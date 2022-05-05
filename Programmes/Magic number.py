"""
A number is said to be a magic number, if the sum of its digits are calculated
till a single digit recursively by adding the sum of the digits after every addition.
If the single digit comes out to be 1,then the number is a magic number.
"""

n= int(input("Enter a number  "))
while (True):
    s=0
    while (n!=0):
        d = n%10
        s = s+d
        n = n//10
    if (s>9):
        n=s
    else:
        break
if (s==1):
    print ("Its a magic number")
else:
    print ("Its not a magic number")