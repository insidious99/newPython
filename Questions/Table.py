# Program to print the multiplication table of a given number.

n = int(input("Enter the number: "))

print("Table of", n)

for i in range(1, 11):
	p = n * i
	print(n, "x", i, "=", p)