l = []
e = 0
o = 0
n = int(input("enter limit"))

for i in range(0, n):
    a = int(input("enter a no."))
    l.append(a)

for i in range(0, len(l)):
    if (l[i] % 2 == 0):
        e = e + 1
    else:
        o = o + 1
print("number of odd numbers present", o)
print("number of even numbers present", e)
