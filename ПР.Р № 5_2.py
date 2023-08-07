slovo = input('введите слово=')
a = slovo.count('a') 
e = slovo.count('e') 
i = slovo.count('i') 
o = slovo.count('o') 
u = slovo.count('u') 
y = slovo.count('y') 
if a == 0: 
    print("a = False") 
if e == 0: 
    print("e = False") 
if i == 0: 
    print("i = False") 
if o == 0: 
    print("o = False") 
if u == 0: 
    print("u = False") 
if y == 0: 
    print("y = False") 
print('Гласных:' , a + e + i + o + u) 
print('Согласных:', len(slovo) - (a + e + i + o + u))
