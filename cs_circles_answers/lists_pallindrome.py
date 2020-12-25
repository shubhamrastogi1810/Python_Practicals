""" This code will check that a string is pallindrome or not. """
def ispalindrome(string):
    """ This function will check that the string is pallindrome or not """
    length = len(string)//2
    count = 0
    while count < length:
        if string[count] == string[len(string)- count-1]:
            temp = 1
        else:
            temp = 0
            break
        count+=1
    if length == 0:
        temp = 1
    if temp == 1:
        return True
    return False

OUTP = ispalindrome(input("String? "))
print(OUTP)
