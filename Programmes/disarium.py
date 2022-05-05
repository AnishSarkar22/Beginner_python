n = int(input("enter a number"))
num = no = n
s = 0
c = 0
while (n != 0):
    c = c + 1
    n = n // 10
while (no != 0):
    d = no % 10
    s = s + d ** c
    c = c - 1
    no = no // 10
if (s == num):
    print("it is a disarium no.")
else:
    print("it is not a disarium no.")
