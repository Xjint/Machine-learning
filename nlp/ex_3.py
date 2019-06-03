from collections import defaultdict
from nltk.corpus import brown
from operator import itemgetter
import nltk
from matplotlib import pyplot as plt

# 创建字典 缺省键的值为0 键：标签 值：标签出现的次数
counts = defaultdict(int)
text = brown.tagged_words(categories='romance', tagset='universal')
for (word, tag) in text:
    counts[tag] += 1
tag_fd = nltk.FreqDist(tag for (word,tag) in text)
tag_fd.plot()
plt.show()

# 按照counts的值进行排序  默认为从小到大 reverse=True则使成为大到小
print('按值排序为（从大到小）：')
print(sorted(counts.items(),key=itemgetter(1),reverse=True))

first_letters = defaultdict(list)
words = brown.words()
for word in words:
    key = word[:2]
    first_letters[key].append(word)
print('首字母为ap的单词为：')
print(first_letters['ap'])
print('共' + str(len(first_letters['ap'])) + '个')



