x = int(input())
if 999<x<10000:
    a = x % 10
    b = x // 10 % 10
    c = x // 100 % 10
    d = x//1000
    print(a + b + c + d)
    print(a*b*c*d)
else:
    print("error")
x = int(input())
if x>=10:
    c=x//10
    e=c%10
    a=x%10
    print(a,e)
else: print("error")

x = int(input())
if 99<x<1000:
     a = x % 10
     b = x // 10 % 10
     c = x // 100 % 10
     z=str(a)+str(b)+str(c)
     g=int(z)-x
     print(g)
else:print("error")

x = int(input())
if 100000<=x<=999999:
     a = x % 10
     b = x //10 % 10
     c = x// 100 % 10
     d= x// 1000 % 10
     e=x// 10000 % 10
     t= x// 100000  
     numbers=[a,b,c,d,e,t]
     print (2 in numbers) 
else:print("error")
    
