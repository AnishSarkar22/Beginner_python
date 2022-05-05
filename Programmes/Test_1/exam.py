import pickle


def countrec():
    f = open("STUDENT.DAT", "rb")
    d = {}
    c = 0
    while True:
        d = p.load(f)
        if d['percentage'] > 75:
            print(d)
            c += 1
    f.close()
    print("no. of student scoring above 75", c)