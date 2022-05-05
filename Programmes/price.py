I = input("enter item name")
Q = int(input("enter item quantity"))
P = float(input("enter price per unit"))
E = Q * P
print(('*' * 16), "BILL", (16 * '*'), "\n")
print("Item name", E, "\t", "Item quantity", Q, "\t", "Item price", P, "\t")
print('*' * 36)
print("total amt to be paid", E)
print('*' * 36)
