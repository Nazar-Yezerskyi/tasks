def function(x):
        return x * 5


def function1(v):
        return v * 3


def main():
    i = -5
    while i < 5:
        i += 0.5
        m = function(i)
        print('function(', i, ') =', m, sep='\t')
        b = function1(i)
        print('function1(', i, ') =', b, sep='\t')


main()
