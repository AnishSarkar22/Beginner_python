l = []
n = int(input("enter limit"))
for i in range(0, n):
    a = int(input("enter number"))
    l.append(a)

ma = max(l)
mi = min(l)
print("the max no.= ", ma)
print("the min no.= ", mi)
