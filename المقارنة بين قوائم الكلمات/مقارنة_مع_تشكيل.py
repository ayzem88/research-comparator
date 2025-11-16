import unicodedata

file1_path = r"قائمة_كلمات_المركز.txt"
file2_path = r"قائمة_مداخل_المعجم.txt"
output_file_path = r"نتائج_الكلمات_المتطابقة.txt"

# قراءة القائمة الأولى
with open(file1_path, 'r', encoding='utf-8') as f:
    list1 = f.read().splitlines()

# قراءة القائمة الثانية
with open(file2_path, 'r', encoding='utf-8') as f:
    list2 = f.read().splitlines()

# إيجاد الكلمات المتطابقة بناءً على الحروف والتشكيل
common_words = set(list1) & set(list2)

# فتح الملف الجديد لحفظ الكلمات المتطابقة
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write("=== الكلمات المتطابقة ===\n")
    
    # كتابة الكلمات المتطابقة وحذفها من القائمتين الأصليتين
    for word in common_words:
        index_in_list1 = list1.index(word)
        index_in_list2 = list2.index(word)
        
        # كتابة الكلمة المتطابقة
        f.write(word + '\n')
        
        # حذف الكلمة من القائمتين الأصليتين
        list1.pop(index_in_list1)
        list2.pop(index_in_list2)

# حفظ القوائم المعدلة بعد الحذف في الملفات الأصلية
with open(file1_path, 'w', encoding='utf-8') as f:
    for word in list1:
        f.write(word + '\n')

with open(file2_path, 'w', encoding='utf-8') as f:
    for word in list2:
        f.write(word + '\n')

print(f"تم حفظ الكلمات المتطابقة في {output_file_path}")

