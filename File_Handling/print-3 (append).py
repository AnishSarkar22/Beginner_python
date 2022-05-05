obj = open("games_list.txt", 'a')
games = ["4) Watchdogs 2\n", "5) PUBG\n", "6) Spiderman \n"]
s = obj.writelines(games)
print(s)
obj.close()

'''
OR
with open("games_list.txt", 'a') as obj:
    games= ["4) Watchdogs 2\n", "5) PUBG\n", "6) Spiderman \n"]
    obj.writelines(games)
'''
