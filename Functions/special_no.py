"""
A special two-digit number is a number such that when the sum of the digits of the number
is added to the product of its digits, the result is equal to the original two-digit number
"""

def specialNumber(n):
    if (n < 10 or n > 99):
        print("Invalid Input! Number",
              " should have 2 digits only")
    else:
        first = n // 10
        last = n % 10
        sum = first + last
        pro = first * last

        if ((sum + pro) == n):

            print(n, " is a Special Two-Digit Number")
        else:

            print(n, " is Not a Special Two-Digit Number")

n= int(input("enter a number  "))
specialNumber(n)