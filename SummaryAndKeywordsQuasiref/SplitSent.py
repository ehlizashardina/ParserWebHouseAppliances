import re
from Sentence import *


class SplitSent:
    #Удаление ненужного
    def modification(a,b):
        for x in b:
             while x in a:
                a.remove(x)
        return a
#выделение слов
    def get_words(text):
        words = [word for word in re.split('n|\s|\)|\(|,|\.|-|\?|:|!', text) if (len(word) > 0 and word != '-')]
        return words

#выделение предложений
    def get_sentences(text):
        pattern = re.compile(r'([А-ЯA-Zа-яa-z]((т.п.|т.д.|пр.)|[^?!.\(]|\([^\)]*\))*[.?!])')
        sentences=[]
        index=0
        for i,sent in enumerate(pattern.findall(text)):
            sentences.append(Sentence(sent[0],index))
            index=index+1
        return sentences




