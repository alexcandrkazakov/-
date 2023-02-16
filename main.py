a=(int(input("Введите число: ")))
c=(complex(input("Введите число")))
if a>20:
    a=a*10
else: print("Ошибка ")
if c!=3+1j:
   c= c**2
else: print("ошибка")
print(a+c)