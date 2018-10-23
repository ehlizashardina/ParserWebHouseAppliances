import re
from SplitSent import *
from Quasiref import *
from pymystem3 import Mystem
import string





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
              punctuation =[' ','','\n','-', ' \n',' – ']

              #получаем список предложений
              listSents=SplitSent.get_sentences(text)

              #получаем нормализованные слова
              for sent in listSents:
                 sent.text=sent.text.translate(str.maketrans('', '', string.punctuation)) #убрали знаки пункутации
                 sent.token = mystem.lemmatize(sent.text) #нормализовали
                 sent.token= SplitSent.modification(sent.token, punctuation) #убрали пустые слова
              
              quasy=Quasiref.Freq(listSents)
              
                   
              

                  
              a=1
              
              
                    
main()