s = "ab"


def fun(d):
    d = d + (d * 2)
    print(d)
    return d[::2]


t = fun(s)
s = fun(t)
print(s)