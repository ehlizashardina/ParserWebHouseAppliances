import re
from SplitSent import SplitSent
def main():
    print ("Введите название файла (например, text.txt):")

    try:
        file=open(input(),'r')
    except IOError as e:
        print("Не удалось открыть файл")
        exit(1)
    else:
        with file:
            print ("Введите процент сжатия от 0 до 100:")
            percent=input()
            if (percent.isnumeric() and int(percent)>=0 and int(percent)<=100):
                text=file.read()
                a=SplitSent.get_sentences(text)
            else: 
                print ("не ок")

    
main()