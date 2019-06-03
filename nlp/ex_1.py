# -*- coding: utf-8 -*-
# coding: utf-8
from nltk.book import *
from matplotlib import pyplot as plt
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
import re

corpus_root = 'D:\\python_wokrspace\\sources\\repo\\nlp'
# wordlists是一个语料库 这个语料库中有2个文件 1.txt  2.txt
wordlists = PlaintextCorpusReader(corpus_root, '.*.txt', encoding='gbk')
wordlists.fileids()
text_1 = wordlists.words(fileids='1.txt')
text_2 = wordlists.words(fileids='2.txt')
stopwords = nltk.corpus.stopwords.words('english')


# 去除奇奇怪怪的符号
def isSymbol(x):
    return bool(re.match(r'[^\w]', x))


# 这个方法用来过滤文章中一些无意义的单词(a the 等等)
def clean_text(text):
    cleaned_text = [t for t in text if t.lower() not in stopwords
                    and not isSymbol(t)]
    return cleaned_text


cleanedtext_1 = clean_text(text_1)
cleanedtext_2 = clean_text(text_2)
fdist1 = FreqDist(cleanedtext_1)
fdist1.plot(30)
fdist2 = FreqDist(cleanedtext_2)
fdist2.plot(30)
words = ['can', 'could', 'may', 'might', 'must', 'will']
genres = ['1.txt', '2.txt']
cfd = nltk.ConditionalFreqDist(
    (cond, word)
    for cond in genres
    for word in wordlists.words(fileids=cond))
cfd.tabulate(samples=words)
cfd.plot(samples=words, conditions=genres)
plt.show()
