s = 4


def f1(x=5):
    global s
    s = s * x
    print(s)


def f2(x=2):
    global s
    print(s ** x)


f1(3)
f2()
f1()
