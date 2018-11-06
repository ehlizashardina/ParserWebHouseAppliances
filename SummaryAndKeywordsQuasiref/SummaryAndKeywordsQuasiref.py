import re
from SplitSent import *
from Quasiref import *
from TF_IDF import *
from pymystem3 import Mystem
import string
import copy




def main():
    print("*******")
    print("ПАСКИ - Программа для автоматического составления краткого изложения")
    print("*******")

    print ("Введите название файла (например, text.txt):")

    try:
        file=open(input(),'r')
    except IOError as e:
        print("Ошибка: Не удалось открыть файл")
        return 
    else:
        with file:
            print ("Введите процент сжатия от 0 до 100:")
            percent=input()
            if not(percent.isnumeric() and int(percent)>=0 and int(percent)<=100):
                print ("Ошибка: Неверное число")
                return
             
            else:
              text=file.read()
              mystem=Mystem()
              punctuation =[' ','','\n','-', ' \n',' – ', '  ']

              #берем обратное значение, используемое в расчетах
              percent = 100 - int(percent)

              #получаем список предложений
              listSents=SplitSent.get_sentences(text)

              #получаем нормализованные слова
              for sent in listSents:
                 text=sent.text.translate(str.maketrans('', '', string.punctuation)) #убрали знаки пункутации
                 sent.token = mystem.lemmatize(text) #нормализовали
                 sent.token= SplitSent.modification(sent.token, punctuation) #убрали пустые слова
              
              listSentsQref = list(listSents)
              listSentsTF_p = copy.deepcopy(listSents)
              
              #listSentsQref=Quasiref.WeightCount(listSentsQref) #получили список предложений с весами
              #f=1
              
              #listSentsTF_p = TF_poiss.WeightCount(listSentsTF_p)
                    
              listSentsQref = Quasiref.RunQuasiref(listSentsQref) #вывод текста квазиреферирование по частоте
              Qreftext = PrintSentences(listSentsQref, percent)
              WriteToFile("qref.txt", Qreftext)
              print('\n\r')
              listSentsTF_p = TF_poiss.RunTF_poiss(listSentsTF_p) #вывод текста квазиреферирование по важности (TF-IDF)
              Tf_ptext = PrintSentences(listSentsTF_p, percent)
              WriteToFile("tf_p.txt", Tf_ptext)
              file.close()
        #finally:

def PrintSentences(listSents, percent):
        numberSent=int(round(len(listSents)*int(percent)/100))
        if numberSent == 0:
            numberSent = 1
        listSents.sort(key=lambda x: x.weight, reverse=True)
        result=[]
        for x in range(numberSent):
                result.append(listSents[x])
        result.sort(key=lambda x: x.index)
    
        newText = "";
        for i in result:
            newText += i.text
        print (newText)
        return newText

def WriteToFile(name, text):
    try:
        file=open(name,'w')
    except IOError as e:
        print("Ошибка: Не удалось открыть или создать файл")
        return 
    else:
        with file:
            file.write(text)
            file.close()

main()