"""
Adam number is a number when reversed, the square of the number and the square
of the reversed number should be numbers which are reverse of each other.
"""

n = int(input("enter a number  "))
num = n
s1 = 0
s2 = 0
ns = n * n
while (num > 0):
    d1 = num % 10
    s1 = s1 * 10 + d1
    num = num / 10
ss = s1 * s1
while (ss > 0):
    d2 = ss % 10
    s2 = s2 * 10 + d2
    ss = ss / 10
if (ns == s2):
    print("its an adam number")
else:
    print("its not an adam number")
