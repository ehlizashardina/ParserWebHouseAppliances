import re
from SplitSent import SplitSent

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
              listSents=SplitSent.get_sentences(text)

              listWords=[]
              for sent in listSents:
                 for  word in SplitSent.get_words(sent):
                    listWords.append(word)
                    print(word)
main()