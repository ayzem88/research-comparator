# استبدل بالمسار الصحيح للملف
input_filename = r"قائمة_كلمات_المركز.txt"

# استبدل بالمسار الذي تريد حفظ الملف الجديد فيه
output_filename = r"قائمة_كلمات_المركز_sorted.txt"

# قراءة الملف وتخزين الكلمات في قائمة
with open(input_filename, 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

# ترتيب الكلمات حسب الحرف الأخير
words.sort(key=lambda word: word[-1])

# كتابة الكلمات المرتبة في الملف الجديد
with open(output_filename, 'w', encoding='utf-8') as file:
    for word in words:
        file.write(word + '\n')
