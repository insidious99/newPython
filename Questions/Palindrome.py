# Program to check if given string is a palindrome.

text = str(input("Enter string: "))
newText = text[::-1]

if text == newText:
	print("Given string is a palindrome.")
else:
	print("Given string is not a palindrome.")