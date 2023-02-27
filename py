x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100 % 10
d = x//1000
print(a + b + c + d)
print(a*b*c*d)

x = int(input())
c=x//10
e=c%10
a=x%10
print(a,e)

x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100 % 10
z=str(a)+str(b)+str(c)
g=int(z)-x
print(g)

x = int(input())

a = x % 10
b = x //10 % 10
c = x// 100 % 10
d= x// 1000 % 10
e=x// 10000 % 10
t= x// 100000  
numbers=[a,b,c,d,e,t]
print (2 in numbers) 
    
