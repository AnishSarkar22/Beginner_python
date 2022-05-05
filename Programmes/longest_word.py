l = []
max = 0
for i in range(0, 10):
    a = input("enter word- ")
    l.append(a)
T = tuple(l)
for w in T:
    if len(w) > max:
        max = len(w)
        maxw = w
print("the longest word-  ", maxw)
