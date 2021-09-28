v = []
a = int(input("Введіть перше значення: "))
b = int(input("Введіть останнє значення: "))
if a < 2 or b < 2:
    print("Некоретні дані")
elif a > b:
    print("Некоретні дані")
else:
    for i in range(a,b):
        prime = True
    for l in range(2,i):
        if i%l == 0:
            prime = False
    if prime:
        print(i)
        v.append(i)
        c = input("Щоб порахувати суму простих чисел введіть 1:\nЩоб закінчити роботу введіть 2:")
        if c == "1":
            print(sum(v))



