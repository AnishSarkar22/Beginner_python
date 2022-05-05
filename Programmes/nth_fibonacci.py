a = 0
b = 1
n = int(input("enter limit"))
print(a)
print(b)
for i in range(0, n):
    a, b = b, a + b
    print(b)
