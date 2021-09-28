def hello(name=str(input("Введіть ім'я"))):
    if len(name) == 0:
        print("Привіт, Назар")
    else:
        print("Привіт,", name)

hello()
