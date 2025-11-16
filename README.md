# مقارنة الأبحاث والكتب / Research and Books Comparator

<div dir="rtl">

## نظرة عامة

أداة متقدمة لمقارنة الأبحاث والكتب النصية العربية. تدعم إظهار الاختلافات والتشابهات بين النصوص مع تحليل N-grams والمقارنة المتقدمة.

## المميزات

- 🔍 **إظهار الاختلافات**: إظهار الاختلافات بين كتابين
- 🔗 **إظهار التشابهات**: إظهار التشابهات بين كتابين
- 📊 **تحليل N-grams**: تحليل التسلسلات النصية
- 📝 **مقارنة القوائم**: مقارنة قوائم الكلمات
- 🧹 **تنظيف النصوص**: تنظيف النصوص وفق رموز محددة
- 📈 **تصدير النتائج**: تصدير النتائج بصيغ Excel و HTML

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- openpyxl
- python-docx (لقراءة ملفات Word)

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/research-comparator.git
cd research-comparator
```

2. قم بتثبيت المتطلبات:
```bash
pip install openpyxl python-docx
```

## الاستخدام

### إظهار الاختلافات بين كتابين

```bash
python "إظهار الاختلافات بين كتابين/الفرق بين ملفين.py"
```

### إظهار التشابهات بين كتابين

```bash
python "إظهار التشابهات بين كتابين/02 - تحويل إلى قوائم للمقارنة/N_Gram.py"
python "إظهار التشابهات بين كتابين/03 - المقارنة/مقارنة للبحث عن المتطابقين.py"
python "إظهار التشابهات بين كتابين/03 - المقارنة/مقارنة للبحث عن المتشابهين.py"
```

### مقارنة قوائم الكلمات

```bash
python "المقارنة بين قوائم الكلمات/مقارنة_مع_تشكيل.py"
python "المقارنة بين قوائم الكلمات/مقارنة_دون_تشكيل.py"
```

## هيكل المشروع

```
مقارنة الأبحاث والكتب/
├── إظهار الاختلافات بين كتابين/
│   ├── الفرق بين ملفين.py
│   └── [ملفات الكتب]
├── إظهار التشابهات بين كتابين/
│   ├── 01 - تنظيف الملف/
│   ├── 02 - تحويل إلى قوائم للمقارنة/
│   └── 03 - المقارنة/
└── المقارنة بين قوائم الكلمات/
    └── [سكريبتات المقارنة]
```

## الملفات الرئيسية

- **الفرق بين ملفين.py**: إظهار الاختلافات
- **N_Gram.py**: تحليل N-grams
- **مقارنة للبحث عن المتطابقين.py**: البحث عن المتطابقين
- **مقارنة للبحث عن المتشابهين.py**: البحث عن المتشابهين

## ملاحظات مهمة

⚠️ **ملاحظة**: 
- البرنامج يدعم ملفات Word و TXT
- يمكن تنظيف النصوص قبل المقارنة
- النتائج تُحفظ بصيغ Excel و HTML

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] تحليل إحصائي متقدم
- [ ] دعم المزيد من صيغ الملفات
- [ ] تصورات بصرية للنتائج

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

An advanced tool for comparing Arabic research papers and books. Supports showing differences and similarities between texts with N-grams analysis and advanced comparison.

## Features

- 🔍 **Show Differences**: Show differences between two books
- 🔗 **Show Similarities**: Show similarities between two books
- 📊 **N-grams Analysis**: Analyze text sequences
- 📝 **List Comparison**: Compare word lists
- 🧹 **Text Cleaning**: Clean texts according to specified symbols
- 📈 **Export Results**: Export results in Excel and HTML formats

## Installation

### Requirements

- Python 3.7 or later
- openpyxl
- python-docx (for reading Word files)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/research-comparator.git
cd research-comparator
```

2. Install requirements:
```bash
pip install openpyxl python-docx
```

## Usage

### Show Differences Between Two Books

```bash
python "إظهار الاختلافات بين كتابين/الفرق بين ملفين.py"
```

### Show Similarities Between Two Books

```bash
python "إظهار التشابهات بين كتابين/02 - تحويل إلى قوائم للمقارنة/N_Gram.py"
python "إظهار التشابهات بين كتابين/03 - المقارنة/مقارنة للبحث عن المتطابقين.py"
python "إظهار التشابهات بين كتابين/03 - المقارنة/مقارنة للبحث عن المتشابهين.py"
```

### Compare Word Lists

```bash
python "المقارنة بين قوائم الكلمات/مقارنة_مع_تشكيل.py"
python "المقارنة بين قوائم الكلمات/مقارنة_دون_تشكيل.py"
```

## Project Structure

```
research-comparator/
├── إظهار الاختلافات بين كتابين/
│   ├── الفرق بين ملفين.py
│   └── [Book files]
├── إظهار التشابهات بين كتابين/
│   ├── 01 - تنظيف الملف/
│   ├── 02 - تحويل إلى قوائم للمقارنة/
│   └── 03 - المقارنة/
└── المقارنة بين قوائم الكلمات/
    └── [Comparison scripts]
```

## Main Files

- **الفرق بين ملفين.py**: Show differences
- **N_Gram.py**: N-grams analysis
- **مقارنة للبحث عن المتطابقين.py**: Search for exact matches
- **مقارنة للبحث عن المتشابهين.py**: Search for similar matches

## Important Notes

⚠️ **Note**: 
- The program supports Word and TXT files
- Texts can be cleaned before comparison
- Results are saved in Excel and HTML formats

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Advanced statistical analysis
- [ ] Support for more file formats
- [ ] Visual representations of results

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

