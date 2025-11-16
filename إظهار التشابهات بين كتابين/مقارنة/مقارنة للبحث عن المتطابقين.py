import pandas as pd

# قراءة البيانات من الملفين مع افتراض أن كل ملف يحتوي على عمود واحد بدون اسم عمود
df1 = pd.read_excel("الجعبري.xlsx", header=None, names=["الجعبري"])
df2 = pd.read_excel("الواحدي.xlsx", header=None, names=["الواحدي"])

# إجراء المقارنة بين البيانات في العمودين
similarities = pd.merge(df1, df2, left_on="الجعبري", right_on="الواحدي", how='inner')

# إذا كنت تريد أن تظهر النتائج في عمودين منفصلين بالأسماء التي وضعتها للأعمدة
similarities = similarities.drop_duplicates()  # إزالة التكرارات إذا لزم الأمر

# كتابة النتائج في ملف إكسل
similarities.to_excel('نتيجة المقارنة بين الملفين.xlsx', index=False)
