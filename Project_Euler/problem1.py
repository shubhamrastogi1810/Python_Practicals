""" this program will print the sum of multiples of 3 or 5 below 1000."""
def main():
    """
    The main function to print sum of multiples of 3 or 5 below 1000.
    """
    add = 0
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            add+=i
    print(add)

if __name__ == "__main__":
    main()
