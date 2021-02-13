""" This program will input a Capital case character and return lowercase. """

def lowerchar(char):
    """ This function will lower the input character."""
    if ord(char) >=65 and ord(char)<=90:
        return chr(ord(char)+ 32)
    return char

output = lowerchar(input("Enter a character "))
print(output)
