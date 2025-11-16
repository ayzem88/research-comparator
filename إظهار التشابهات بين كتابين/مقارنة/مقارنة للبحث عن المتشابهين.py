import pandas as pd
from rapidfuzz import fuzz, process

# قراءة البيانات من الملفين
df1 = pd.read_excel("أسباب_النزول_الجعبري.txt.xlsx", header=None, names=["الجعبري"])
df2 = pd.read_excel("أسباب_النزول_الميمان.txt.xlsx", header=None, names=["الواحدي"])

# تحويل العمود الثاني إلى قائمة للتحقق من التشابه
choices = df2["الواحدي"].tolist()

# استخدام process.extract بدلاً من التكرار المزدوج لمقارنة كل جملة في df1 مع جميع الجمل في df2
def get_matches(query, choices, limit=1):
    results = process.extract(query, choices, scorer=fuzz.partial_ratio, limit=limit)
    for result in results:
        if result[1] > 80:
            return result[0], result[1]
    return None, None

# تطبيق الدالة على كل جملة في df1
df1["matches"] = df1["الجعبري"].apply(lambda x: get_matches(x, choices))

# توسيع النتائج إلى عمودين جديدين
df1["الواحدي المتشابه"], df1["نسبة التشابه"] = zip(*df1["matches"])

# إزالة الصفوف التي لا تحتوي على تطابقات
df1 = df1.dropna(subset=["الواحدي المتشابه"])

# إزالة العمود المساعد
df1.drop("matches", axis=1, inplace=True)

# كتابة النتائج في ملف إكسل
df1.to_excel('نتيجة المقارنة بين الملفين.xlsx', index=False)
