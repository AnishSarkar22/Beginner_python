obj = open("poem.txt", 'r')
s = obj.read()
print(len(s), "bytes")
obj.close()

'''
OR
with open("poem.txt", 'r') as obj:
    s = obj.read()
    print(len(s), "bytes")
'''