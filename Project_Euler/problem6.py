"""
The code computes the difference of sum of square and square of the sum of first 100 natural numbers
"""
def main():
    """
    This function prints the difference of sum square and square of the sums of 100 natural numbers
    """
    # sum of the squares of first 100 natural numbers.
    sumsq = 0
    for i in range(1,101):
        sumsq += i**2


    # square of the sum of first 100 natural numbers.
    sums = 0
    for i in range(1,101):
        sums += i
    sums = sums**2
    print(sums - sumsq)

if __name__ == "__main__":
    main()
