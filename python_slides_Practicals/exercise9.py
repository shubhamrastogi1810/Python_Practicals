""" program to input catch -ve in number and ask for tolerance and catch -ve"""
text = input('Number? ')
number = float(text)
if number < 0:
    print("Number is negative")
else:
    if number < 1.0:
        LOWER = number
        UPPER = 1.0
    else:
        LOWER = 1.0
        UPPER = number

    temp_no = input("Tolerance? ")
    tolerance = float(temp_no)
    if tolerance < 0:
        print("No negative tolerance ")
    else:
        uncertainty = UPPER - LOWER

        while uncertainty > tolerance:
            middle = (LOWER + UPPER) / 2

            if middle ** 2 < number:
                LOWER = middle
            else:
                UPPER = middle

        print(LOWER, UPPER)
        uncertainty = UPPER - LOWER
