from SplitSent import *
#from stop_words import stop_words
from collections import OrderedDict
from Sentence import *
#import numpy as np
from scipy.stats import poisson
#import math

class TF_poiss:

    def Freq(listSents): #подсчет частот
         all_words_count = 0
         diction = {}
        #for i in listSents: #подсчитываем частоту слов в предложениях и встречаемость по предложениям (только есть или нет)
            #i.token_count=0
            #for x in i.token:
            #    if x in i.dictinary:
            #        i.dictionary[x]+=1
            #    else:
            #        i.dictionary[x] = 1
            #        if x in diction:
            #            diction[x]+=1
            #        else:
            #            diction[x] = 1
            #    #i.token_count+=1
         for i in listSents: #подсчитываем частоту слов в предложениях и общее кол-во
            #i.token_count=0
            for x in i.token:
                if x in diction:
                    diction[x]+=1
                else:
                    diction[x] = 1
                all_words_count+=len(i.token)
                #i.token_count+=1

         for (key, value) in diction.items():
             diction[key] = value * 100 / all_words_count

         sorted_dict = sorted(diction.items(), key=lambda x:x[1], reverse=True) #сортируем по относительной частоте по убыванию
         return dict(sorted_dict)

    def WeightCount(listSents): #подсчёт весов предложений
         diction = TF_poiss.Freq(listSents)
         dist = poisson(4)
         for x in range(len(diction)): #считаем важность (вероятность) по распеределению
            diction[x] = dist.pmf(x)

         for sent in listSents: #считаем вес каждого предложения
            for x in sent.token:
                if x in diction:
                    sent.weight+=diction[x]
            sent.weight /= len(sent.token)
         return listSents

    def RunTF_poiss(listSents, percent):
        listSents=TF_poiss.WeightCount(listSents) #получили список предложений с весами
        numberSent=int(round(len(listSents)*int(percent)/100))
        listSents.sort(key=lambda x: x.weight, reverse=True)
        result=[]
        for x in range(numberSent):
                result.append(listSents[x])
        result.sort(key=lambda x: x.index)
    
        newText = "";
        for i in result:
            newText += i.text;
        print (newText)