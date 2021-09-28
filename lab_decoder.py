a = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцШшЩщЬьЮюЯя" \
    "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz" \
    "1234567890"
then = 0

while True:
    b = input("Введіть текст:")
    g = ""
    for i in b:
        now = a.find(i)
        step = 2
        if now >= 114:
            step = 1
            if now == 114:
                step -= 10
        if now == 0:
            step -= 64
        if now == 1:
            step -= 64
        if now == 64:
            step -= 50
        if now == 65:
            step -= 50

        then = now - step
        if i in a:
            g += a[then]
        else:
            g += i

    print(g)