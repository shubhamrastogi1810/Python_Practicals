""" This program inputs a string and returns lowercase string with lowerchar() function."""
# 11 A program of cs circles.
def lowerchar(char):
    """ This function will lower the input character."""
    if ord(char) >=65 and ord(char)<=90:
        return chr(ord(char)+ 32)
    return char

def lowerstring(strin):
    """This function will input a string and will convert it to lowercase string """
    newstr=''
    for i in strin:
        newstr+=lowerchar(i)
    return newstr

output = lowerstring(input("Enter a string "))
print(output)
