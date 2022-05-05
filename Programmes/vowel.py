#to find the words starting with vowel

l = []
for i in range(0, 10):
    a = input("enter word- ")
    l.append(a)
t = tuple(l)
print("The words starting with vowels are:")
for w in t:
    if (w[0] == "A" or w[0] == "a" or w[0] == "E" or w[0] == "e" or w[0] == "I" or w[0] == "i" or w[0] == "O" or
            w[0] == "o" or w[0] == "U" or w[0] == "u"):
        print(w)
