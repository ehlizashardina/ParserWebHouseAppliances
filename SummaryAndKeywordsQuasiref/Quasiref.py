from SplitSent import *
from stop_words import stop_words
from collections import OrderedDict
from Sentence import *

class Quasiref:

    def Freq(listSents): #подсчет частот
        for sent in listSents:
             sent.token = SplitSent.modification(sent.token, stop_words) #убрали стоп-слова
        
        diction = {}
        for i in listSents: #подсчитываем частоту слов
            for x in i.token:
                if x in diction:
                    diction[x]+=1
                else:
                    diction[x] = 1

        copy_dict = dict(diction) #удаляем слова с частотой = 1
        for (key, value) in copy_dict.items():
            if value == 1:
                del diction[key]

        sorted_dict = sorted(diction.items(), key=lambda x:x[1], reverse=True) #сортируем по частоте по убыванию
        return dict(sorted_dict)

    def WeightCount(listSents): #подсчёт весов предложений
        diction = Quasiref.Freq(listSents)
        for sent in listSents:
            for x in sent.token:
                if x in diction:
                    sent.weight+=diction[x]
        return listSents 

    def RunQuasiref(listSents):
        listSents=Quasiref.WeightCount(listSents) #получили список предложений с весами
        return listSents

        