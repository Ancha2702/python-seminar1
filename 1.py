#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
day= int(input("Введите день недели:\n"))
if day>0 and day<8:
    if day==1:
        print("Понедельник")
    if day==2:
        print("Вторник")
    if day==3:
        print("Среда")
    if day==4:
        print("Четверг")
    if day==5:
        print("Пятница")
    if day==6:
        print("Суббота")
    if day==7:
        print("Воскресенье")
else:
    print("Такого дня недели нет")