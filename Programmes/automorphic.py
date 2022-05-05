# To check whether the number is Automorphic number or not.
# A number is called Automorphic number if and only if its square ends in the same digits as the number itself.


n = int(input("Enter a no.-  "))
m = n * n
c = 0
p = n
while p != 0:
    c = c + 1
    p = p // 10
a = 10 ** c
if m % a == n:
    print("Automorphic no.")
else:
    print("Not Automorphic no. ")
