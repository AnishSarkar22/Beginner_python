c = 0
n = int(input("enter a number  "))
for i in range(1, n + 1):
    if n % i == 0:
        c = c + 1
if c == 2:
    print("Its a prime no.")
else:
    print("Its not a prime no.")
