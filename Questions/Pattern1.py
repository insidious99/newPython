# Program to print following pattern.
# *
# **
# ***
# ****

n= int(input("Enter the number: "))

for a in range(1, n + 1):
	for b in range(1, a + 1):
		print("*", end = "")
	print()