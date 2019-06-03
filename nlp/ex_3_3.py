from nltk.corpus import brown
import nltk
from matplotlib import pyplot as plt
import numpy as np
from pickle import dump
from pickle import load

def performance(cfd, wordlist):
    # cfd[word].max()表示word出现最频繁的那个词性
    lt = dict((word, cfd[word].max()) for word in wordlist)
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(model=lt, backoff=t0)
    t2 = nltk.BigramTagger(model=lt, backoff=t1)
    t3 = nltk.TrigramTagger(model=lt, backoff=t2)
    output = open('tar.pkl','wb')
    dump(t3,output,-1)
    output.close()
    return t3.evaluate(brown.tagged_sents(categories='news'))


def display():
    # 统计news中的高频词汇  （词汇，出现次数）
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    # 单独提取出这些词汇
    words_by_freq = [w for (w, _) in word_freqs]
    # cfd记录了每个单词 与它对应的各个词性出现的次数
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** np.arange(0, 15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    plt.plot(sizes, perfs)
    plt.show()


display()
input = open('tar.pkl','rb')
tagger = load(input)
input.close()
text = """The board's action shows what free enterprise
...     is up against in our complex maze of regulatory laws ."""
tokens = text.split()
print(tagger.tag(tokens))
