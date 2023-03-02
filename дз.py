x=int(input("Введите трехзначное число "))
if 99<x<1000:
    a = x // 100 % 10
    b= x//10 % 10
    c= x//100
else: print("error")
if 9<a+b+c<100:
    print("двухзначное")
else:print("не двухзначное")

x=int(input("Введите трехзначное число "))
if 99<x<1000:
    a = x // 100 % 10
    b= x//10 % 10
    c= x//100
else: print("error")
if 99<a*b*c<1000:
    print("трехзначное")
else:print("не трехзначное")

x=int(input("Введите трехзначное число "))
a=int(input("Введите число "))
if 99<x<1000:
    j = x // 100 % 10
    b= x//10 % 10
    c= x//100
else: print("error")
if j*b*c>a :
    print("больше")
else:print("не больше")

x=int(input("Введите трехзначное число "))
if 99<x<1000:
    j = x // 100 % 10
    b= x//10 % 10
    c= x//100
else: print("error")
if (j+b+c)/5*10%10==0 :
    print("кратное")
else:print ("не краткое")

x=int(input("Введите трехзначное число "))
a=int(input("Введите число "))
if 99<x<1000:
    j = x // 100 % 10
    b= x//10 % 10
    c= x//100
else: print("error")
if (j+b+c)%a==0 :
    print("кратное")
else:print ("не краткое")

