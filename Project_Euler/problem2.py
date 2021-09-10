""" This program will print the sum of even-valued terms upto 4 million of a fibonacci series."""

def main():
    """
    This function prints sum of even-valued terms upto 4M fibonacci.
    """

    first = 1
    second = 2
    eve_add = 2

    while first + second <= 4000001:

        add = first + second

        if add % 2 == 0:
            eve_add += add

        first = second
        second = add

    print(eve_add)

if __name__ == "__main__":
    main()
