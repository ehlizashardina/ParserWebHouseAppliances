import re

class SplitSent:

#выделение слов
    def get_words(text):
        words = [word for word in re.split('n|\s|\)|\(|,|\.|-|\?|:|!', text) if (len(word) > 0 and word != '-')]
        return words

#выделение предложений
    def get_sentences(text):
        pattern = re.compile(r'([А-ЯA-Zа-яa-z]((т.п.|т.д.|пр.)|[^?!.\(]|\([^\)]*\))*[.?!])')
        sentences=[]
        for i,sent in enumerate(pattern.findall(text)):
            sentences.append(sent[0])
        return sentences


