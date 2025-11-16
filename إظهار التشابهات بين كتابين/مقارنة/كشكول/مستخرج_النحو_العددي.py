import os
import pandas as pd
from collections import Counter
path = r"E:\مقارنة الأبحاث والكتب\إظهار التشابهات بين كتابين\مقارنة"
n = 7
for filename in os.listdir(path):
  with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
    text = file.read()
  words = text.split()
  ngrams = [words[i:i+n] for i in range(len(words)-n+1)]
  ngrams_flattened = [' '.join(ngram) for ngram in ngrams]
  ngrams_counted = Counter(ngrams_flattened)
  ngrams_counted_list = [(ngram, count) for ngram, count in ngrams_counted.items()]
  chunk_size = 1048576
  chunks = [ngrams_counted_list[i:i+chunk_size] for i in range(0, len(ngrams_counted_list), chunk_size)]
  writer = pd.ExcelWriter(f'{filename}.xlsx', engine='xlsxwriter')
  for i, chunk in enumerate(chunks):
    df = pd.DataFrame(chunk, columns=['ngram', 'count'])
    df.to_excel(writer, index=False, sheet_name=f'sheet{i+1}')
  writer.close()
print('انتهى!')
