# Program to print following pattern
# A
# BB
# CCC
# DDDD

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print(chr(ord('A') + i), end="")
    print()

