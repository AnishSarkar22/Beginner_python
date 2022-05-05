obj = open("poem.txt", 'r')
s = obj.readlines()
print(len(s), "lines are present")
obj.close()

'''
OR
with open("poem.txt", 'r') as obj:
    s = obj.readlines()
    print(len(s), "lines are present")
'''
