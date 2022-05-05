s=input("enter a string  ")
x=" "
s=s+" "
l=len(s)
for i in range (1,l+1):
    if (s[i]!=" "):
        x=x+s
    else:
        print (\n x)
        x=" "
