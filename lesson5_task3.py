
def number1():
    while True:
        try:
            number = float(input("Введіть число 1"))
            return number
        except ValueError:
            print("Некоректні дані! Спробуйте ще раз")


def number2():
    while True:
        try:
            numberc = float(input("Введіть число 2"))
            return numberc
        except ValueError:
            print("Некоректні дані! Спробуйте ще раз ")




def addition(number,numberc):
    m = number + numberc
    print(m)

def substraction(a,b):
    m = a - b
    print(m)

def multiplication(a,b):
    m = a * b
    print(m)

def division(a,b):
    if b !=0:
        m = a / b
        print(m)
    else:
        print("Ділення на нуль")

def x():
    a = number1()
    b = number2()

    r = input("Дія")
    if r == "+":
        addition(a,b)
    elif r == "-":
        substraction(a,b)
    elif r == "*":
        multiplication(a,b)
    elif r == "/":
        division(a,b)





while True:
    x()
    f = input("Щоб продовжити виберіть 1 \nЩоб закінчтити робоу виберіть 2")
    if f == "2":
        break
