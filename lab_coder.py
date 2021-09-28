a = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя" \
    "AaBbCcDdEeFfJjHhIiGgKkLlMmNnOoPpQqRrSsTtUuWwXxZz" \
    "1234567890"
then = 0

while True:
    g = ""
    b = input("Введіть текст: ")
    for i in b:
        now = a.find(i)
        step = 2
        if now >= 114:
            step = 1
            if now == 123:
                step -= 10

        if now == 64:
            step -= 66
        if now == 65:
            step -= 66
        if now == 112:
            step -= 48
        if now == 113:
            step -= 48

        then = now + step
        if i in a:
            g += a[then]
        else:
            g += i

    print(g)