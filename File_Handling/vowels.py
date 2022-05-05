# Words starting with vowels in a file

f1 = open("poem.txt", "r")

k = []
c = 0
for l in f1:
    k = l.split()
    if k[0][0] in 'AEIOUaeiou':
        c = c + 1
print(c)
f1.close()