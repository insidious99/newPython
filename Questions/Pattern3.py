# Program to print the following pattern
# 1
# 22
# 333
# 4444

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()
