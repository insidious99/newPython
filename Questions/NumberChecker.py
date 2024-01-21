# Program to check if given number is
# positive, negative or zero.

n = float(input("Enter the number: "))

if n > 0:
	print(n, "is positive.")
elif n == 0:
	print(n, "is zero.")
elif n < 0:
	print(n, "is negative.")