"""A Kaprekar number is a number whose square when divided into two parts and such
that sum of parts is equal to the original number and none of the parts has value 0.
"""

n = int(input("enter a number  "))
c = 0
num = n
sq = n * n
while (n > 0):
    n = n / 10
    c = c + 1
p = 10 ** c
if ((sq % p) + (sq / p) == num):
    print("its a kapreaker number")
else:
    print("its not a kapreaker number")
