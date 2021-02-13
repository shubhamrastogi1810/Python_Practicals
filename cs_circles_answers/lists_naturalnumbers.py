""" This file takes a positive number as input, returns a list of nos. upto that number."""

def naturalnumbers(number):
    """This function will return a list of numbers upto an input number"""
    num_lis = [0]*number
    for i in range(0,number):
        num_lis[i] = i+1
    return num_lis

numb = int(input("Enter a number "))
LIST = naturalnumbers(numb)
print(LIST)
