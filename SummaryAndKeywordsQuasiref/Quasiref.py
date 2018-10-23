from SplitSent import *
from stop_words import stop_words
from collections import OrderedDict
from Sentence import *

class Quasiref:
     

    def Freq(listSents):
        for sent in listSents:
             sent.token=SplitSent.modification(sent.token, stop_words) #убрали стоп-слова
        
        diction={}
        for i in listSents: #подсчитываем частоту слов
            for x in i.token:
                if x in diction.keys():
                    diction[x]+=1
                else:
                    diction[x]=1

        copy_dict=dict(diction)
        for (key, value) in copy_dict.items() :
            if value == 1:
                del diction[key]

        sorted_dict = sorted(diction.items(), key=lambda x:x[1], reverse=True)
        sorted_dict=dict(sorted_dict)

        for sent in listSents:
           for x in sent.token:
              if x in sorted_dict:
               sent.weight+=sorted_dict[x]

       
       

        return sorted_dict
     