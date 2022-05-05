obj = open("games_list.txt", 'w')
games = ["1) GTA V\n", "2) Fortnite\n", "3) FIFA 20\n"]
s = obj.writelines(games)
print(s)
obj.close()

'''
OR
with open("games_list.txt", 'w') as obj:
    games= ["1) GTA V\n", "2) Fortnite\n", "3) FIFA 20\n"]
    obj.writelines(games)
'''
