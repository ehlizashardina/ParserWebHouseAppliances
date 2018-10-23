from SplitSent import *
from stop_words import stop_words
from collections import OrderedDict
from Sentence import *
#import math

class TF_IDF:

	def Freq(listSents): #подсчет частот
		all_words_count = 0
		diction = {}
   #     for i in listSents: #подсчитываем частоту слов в предложениях и встречаемость по предложениям (только есть или нет)
			#i.token_count=0
			#for x in i.token:
			#	if x in i.dictinary:
			#		i.dictionary[x]+=1
			#	else:
			#		i.dictionary[x] = 1
			#		if x in diction:
			#			diction[x]+=1
			#		else:
			#			diction[x] = 1
			#	#i.token_count+=1
		for i in listSents: #подсчитываем частоту слов в предложениях и общее кол-во
			#i.token_count=0
			for x in i.token:
				if x in diction:
					diction[x]+=1
				else:
					diction[x] = 1
				all_words_count+=i.token.count
				#i.token_count+=1

		for i in diction:
			i = i / all_words_count
        #copy_dict = dict(diction) #удаляем слова с частотой = 1
        #for (key, value) in copy_dict.items():
        #    if value == 1:
        #        del diction[key]


        sorted_dict = sorted(diction.items(), key=lambda x:x[1], reverse=False) #сортируем по относительной частоте по возрастанию
		return dict(sorted_dict)

	def WeightCount(listSents): #подсчёт весов предложений
        diction = TF_IDF.Freq(listSents)
        for sent in listSents:
            for x in sent.token:
                if x in diction:
                    sent.weight+=diction[x]
        return listSents


