# Program to swap values of two variables

var1 = input("Enter a variable: ")
var2 = input("Enter a variable: ")

print("Before swapping, variable-1 is", var1,"and variable-2 is", var2 )

temp = var1
var1 = var2
var2 = temp

print("After swapping, variable-1 is", var1, "and variable-2 is", var2)