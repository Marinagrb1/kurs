a = int(input('a='))
if a > 0 and a % 2 == 0:
    print('положительное и четное')
elif a > 0 and a % 2 == 1:
   print('положительное и нечетное') 
elif a < 0 and a % 2 == 0:
    print('отрицательное и четное')
elif a < 0 and a % 2 == 1:
   print('отрицательное и нечетное') 
else:
    print('нулевое')
