obj = open("poem.txt", 'r')

for line in obj:
    print(line, end=' ')
obj.close()

"""

line = obj.readline()
while line != '':
    print(line, end='')
    line = obj.readline()
"""