""" program to print Fibonacci Series up to an Input Limit with a function."""
def print_fibonacci(last):
    """This function will print fibonacci series up to the inputed number."""
    first = 0
    second = 1
    print(first,second, sep='\n')
    while True:
        total = first + second
        if total < last:
            print(total)
            first = second
            second = total
        else:
            break
value = int(input("Enter the limit number.-> "))
print_fibonacci(value)
