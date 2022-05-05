s = []
for i in range(0, 10):
    n = int(input("enter number"))
    s.append(n)

for i in range(0, 10):
    c = 0
    for j in range(1, s[i] + 1):
        if (s[i] % j == 0):
            c = c + 1
    if (c == 2):
        print(s[i])
