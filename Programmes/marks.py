s = []
g = []
for i in range(0, 10):
    n = input("enter name  ")
    m = int(input("enter marks  "))
    s.append(n)
    g.append(m)

for i in range(0, 10):
    if g[i] > 80:
        print(s[i])
        print(g[i])
