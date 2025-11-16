def sort_and_save_words_by_length(file_path, output_file_path):
    try:
        # قراءة البيانات من الملف
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # تخزين الكلمات مع طولها في قائمة من الأزواج
        words_with_lengths = []
        for line in lines:
            word = line.strip()  # إزالة الفراغات حول الكلمة
            word_length = len(word)  # حساب طول الكلمة
            words_with_lengths.append((word_length, word))
        
        # ترتيب القائمة بناءً على طول الكلمات من الأصغر إلى الأكبر
        sorted_words = sorted(words_with_lengths, key=lambda x: x[0])
        
        # كتابة النتائج إلى ملف جديد
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for length, word in sorted_words:
                output_file.write(f'{length} {word}\n')
                
        print("تم حفظ النتائج بنجاح.")
            
    except Exception as e:
        print(f"حدث خطأ: {e}")

# المسار الخاص بملف الإدخال
file_path = r"قائمة_كلمات_المركز.txt"
# المسار الخاص بملف الإخراج
output_file_path = r"قائمة_كلمات_المركز_Sort.txt"

sort_and_save_words_by_length(file_path, output_file_path)
