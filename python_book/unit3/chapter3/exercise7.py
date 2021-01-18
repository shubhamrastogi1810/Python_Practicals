""" This program will generte and print factorial number up to a input number."""
def print_factorial(number):
    """ This function will print factorial up to the input number."""
    for i in range(1,number+1):
        factorial = 1
        count = i
        while count >= 1:
            factorial *= count
            count -= 1
        print(str(i)+"! = "+str(factorial))
value = int(input("Enter the number upto you want factorial-> "))
print_factorial(value)
