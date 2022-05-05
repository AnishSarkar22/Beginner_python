s = 0
a = 0
f = 1
n = int(input("enter a number  "))
for i in range(1, n + 1):
    s = s + (i + (i + 1)) / (i * (i + 1))
print("the sum =", s)
