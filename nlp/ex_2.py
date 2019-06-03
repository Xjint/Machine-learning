# 导入必要库  读入文件
# -*- coding: <coding> -*-
import nltk, re, pprint
from nltk import word_tokenize

f = open('1.txt')
raw = f.read()
f.close()
# tokens是所有词的列表
tokens = word_tokenize(raw)
# 将所有字母小写
words = [w.lower() for w in tokens]
# set将word中重复项去掉 sorted用来排序
vocab = sorted(set(words))
# 以abc开头 ing结尾的单词
begin_abc_end_ing = [w for w in vocab if re.search('^[abc].*ing$', w)]
print(begin_abc_end_ing)
# 将raw分割成句子列表
sents = nltk.sent_tokenize(raw)
pprint.pprint(sents[:3])
# 忽略词内部的元音 在tokens即原词表上操作
p = r'^[aeiouAEIOU]+|[aeiouAEIOU]+$|[^aeiouAEIOU]'


def change(word):
    w = re.findall(p, word)
    return ''.join(w)


new_words = [change(w) for w in tokens]
# tokenwrap()可以将单词列表还原成文章
print(nltk.tokenwrap(new_words))
f = open('out_put.txt', 'w')
f.write(nltk.tokenwrap(new_words))
