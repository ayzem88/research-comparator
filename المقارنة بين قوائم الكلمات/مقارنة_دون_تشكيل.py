import unicodedata

def remove_diacritics(word):
    """إزالة التشكيل والحركات من الكلمة"""
    return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')

file1_path = r"قائمة_كلمات_المركز.txt"
file2_path = r"قائمة_مداخل_المعجم.txt"
output_file_path = r"نتائج_الكلمات_ألمتطابقة_دون تشكيل.txt"

# قراءة القائمة الأولى
with open(file1_path, 'r', encoding='utf-8') as f:
    list1 = f.read().splitlines()

# قراءة القائمة الثانية
with open(file2_path, 'r', encoding='utf-8') as f:
    list2 = f.read().splitlines()

# إنشاء نسخ غير مشكلة من القائمتين
list1_no_diacritics = [remove_diacritics(word) for word in list1]
list2_no_diacritics = [remove_diacritics(word) for word in list2]

# إيجاد الكلمات المتطابقة بناءً على الحروف فقط
common_words = set(list1_no_diacritics) & set(list2_no_diacritics)

# فتح الملف الجديد لحفظ الكلمات المتطابقة
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write("=== الكلمات المتطابقة ===\n")
    
    # كتابة الكلمات المتطابقة وحذفها من القائمتين الأصليتين
    for word in common_words:
        index_in_list1 = list1_no_diacritics.index(word)
        index_in_list2 = list2_no_diacritics.index(word)
        
        # كتابة الكلمة المتطابقة
        f.write(list1[index_in_list1] + '\n')
        
        # حذف الكلمة من القائمتين الأصلية والمشكلة
        list1.pop(index_in_list1)
        list1_no_diacritics.pop(index_in_list1)
        list2.pop(index_in_list2)
        list2_no_diacritics.pop(index_in_list2)

# حفظ القوائم المعدلة بعد الحذف في الملفات الأصلية
with open(file1_path, 'w', encoding='utf-8') as f:
    for word in list1:
        f.write(word + '\n')

with open(file2_path, 'w', encoding='utf-8') as f:
    for word in list2:
        f.write(word + '\n')

print(f"تم حفظ الكلمات المتطابقة في {output_file_path}")
