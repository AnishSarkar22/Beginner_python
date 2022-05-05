# Read lines from a text file & display those words which are less than 4 characters

def display():
    file = open("story.txt", 'r')
    line = file.read()
    word = line.split()
    for w in word:
        if len(w) < 4:
            print("words are-  ", w, end=',')
    file.close()
