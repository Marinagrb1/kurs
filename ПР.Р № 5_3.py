x=int(input('минимальная сумма инвестиций'))
a=int(input(' сколько денег у Майкла? '))
b=int(input(' сколько денег у Ивана? '))
if a>=x and b>=x:
    print('2')
elif a>=x and b<x:
    print('Mike')
elif a<x and b>=x:
    print('Ivan')  
elif a<x and b<x and (a+b)>=x:
    print('1')
else:
    print('0')