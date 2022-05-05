"""
A special two-digit number is a number such that when the sum of the digits of the number
is added to the product of its digits, the result is equal to the original two-digit number
"""

n = int(input("enter a number  "))
no=n
s= 0
p= 1
while (no > 0):
    f = n % 10
    l = n // 10
    p = f * l
    s= f + l
    t = s + p
    no=no //10
if (t == n):
    print("its a special number")
else:
    print("its not a special number")
