import time, difflib, re
from docx import Document

def remove_diacritics(text):
    # إزالة الحركات (التشكيل) من النص
    return re.sub(r'[\u064B-\u0652]', '', text)

def diff_chars(old, new, side):
    """مقارنة حرفية لكلمتين تختلفان في الحركات فقط"""
    s = difflib.SequenceMatcher(None, list(old), list(new))
    result = ""
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == "equal":
            result += (old[i1:i2] if side=="left" else new[j1:j2])
        else:
            color = "red" if side=="left" else "lightgreen"
            result += f'<span style="background-color: {color};">' + (old[i1:i2] if side=="left" else new[j1:j2]) + '</span>'
    return result

def diff_line(old_line, new_line):
    """مقارنة سطر بكلمة، مع تظليل:
       - في حالة الإضافة: الكلمة المضافة فقط (بالأخضر)
       - في حالة الحذف: تظليل الكلمة التي قبل الحذف وبعده (بالأصفر) في النص القديم
       - وإذا كان الفرق في التشكيل فقط، يتم تظليل الحرف المختلف"""
    old_words = old_line.split()
    new_words = new_line.split()
    s = difflib.SequenceMatcher(None, old_words, new_words)
    res_old, res_new = [], []
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == "equal":
            res_old.extend(old_words[i1:i2])
            res_new.extend(new_words[j1:j2])
        elif tag == "insert":
            # تظليل الكلمة المضافة فقط في النص الجديد
            for word in new_words[j1:j2]:
                res_new.append(f'<span style="background-color: lightgreen;">{word}</span>')
        elif tag == "delete":
            # عند حذف كلمة، نظلل الكلمة التي قبل وبعدها (إن وُجدت) في النص القديم
            context = []
            if i1 - 1 >= 0:
                context.append(f'<span style="background-color: yellow;">{old_words[i1-1]}</span>')
            if i2 < len(old_words):
                context.append(f'<span style="background-color: yellow;">{old_words[i2]}</span>')
            res_old.extend(context)
        elif tag == "replace":
            block_old = old_words[i1:i2]
            block_new = new_words[j1:j2]
            if len(block_old) == len(block_new):
                for wo, wn in zip(block_old, block_new):
                    # إذا كانت الكلمتان تختلفان فقط في التشكيل
                    if remove_diacritics(wo) == remove_diacritics(wn):
                        res_old.append(diff_chars(wo, wn, "left"))
                        res_new.append(diff_chars(wo, wn, "right"))
                    else:
                        res_old.append(f'<span style="background-color: red;">{wo}</span>')
                        res_new.append(f'<span style="background-color: lightgreen;">{wn}</span>')
            else:
                res_old.append(f'<span style="background-color: red;">{" ".join(block_old)}</span>')
                res_new.append(f'<span style="background-color: lightgreen;">{" ".join(block_new)}</span>')
    return ' '.join(res_old), ' '.join(res_new)

def split_paragraph_into_lines(paragraph, max_words_per_line):
    words = paragraph.split()
    for i in range(0, len(words), max_words_per_line):
        yield ' '.join(words[i:i+max_words_per_line])

def read_docx(file, max_words_per_line):
    doc = Document(file)
    lines = []
    for para in doc.paragraphs:
        for line in split_paragraph_into_lines(para.text, max_words_per_line):
            lines.append(line)
    return lines

start = time.time()
first_file = "القديم.docx"
second_file = "الجديد.docx"

old_lines = read_docx(first_file, 15)
new_lines = read_docx(second_file, 15)

# محاذاة السطور بين الملفين باستخدام SequenceMatcher
s = difflib.SequenceMatcher(None, old_lines, new_lines)
html_rows = []
for tag, i1, i2, j1, j2 in s.get_opcodes():
    if tag == "equal":
        for old, new in zip(old_lines[i1:i2], new_lines[j1:j2]):
            html_rows.append(f"<tr><td>{old}</td><td>{new}</td></tr>")
    else:
        old_chunk = old_lines[i1:i2]
        new_chunk = new_lines[j1:j2]
        max_len = max(len(old_chunk), len(new_chunk))
        for i in range(max_len):
            o = old_chunk[i] if i < len(old_chunk) else ""
            n = new_chunk[i] if i < len(new_chunk) else ""
            diff_o, diff_n = diff_line(o, n)
            html_rows.append(f"<tr><td>{diff_o}</td><td>{diff_n}</td></tr>")

html = f"""<html>
<head>
<meta charset="utf-8">
<style>
  body {{ direction: rtl; }}
  table {{ width: 100%; border-collapse: collapse; }}
  td {{ border: 1px solid #ccc; padding: 5px; vertical-align: top; }}
</style>
</head>
<body>
<table>
<tr><th>القديم</th><th>الجديد</th></tr>
{''.join(html_rows)}
</table>
</body>
</html>"""

with open("difference_report.html", "w", encoding="utf-8") as f:
    f.write(html)

end = time.time()
print("انتهى البرنامج")
print("استغرقت المقارنة حوالي: " + str(end - start))
