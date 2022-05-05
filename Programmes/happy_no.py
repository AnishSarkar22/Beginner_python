"""
A number is called happy if it leads to 1 after a sequence of steps wherein each
 step number is replaced by the sum of squares of its digit that is if we start with Happy Number
 and keep replacing it with digits square sum, we reach 1.
"""

n= int(input("Enter a number  "))
while (True):
    s=0
    while (n!=0):
        r = n%10
        s = s+(r**2)
        n = n//10
    if (s>9):
        n=s
    else:
        break
if (s==1):
    print ("Its a happy number")
else:
    print ("Its not a happy number")