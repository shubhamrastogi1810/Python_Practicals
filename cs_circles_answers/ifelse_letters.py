""" This code inputs a capital character, gives its position as output in 1 to 26. """
letter = input("Enter the character")
if ord(letter)>=65 and ord(letter)<=90:
    print(ord(letter)-64)
else:
    print("invalid")
