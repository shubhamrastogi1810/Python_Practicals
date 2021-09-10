"""
    This code will do summation of answer of individual numbers of a number raised to power.
"""
def main():
    """
    This function adds the digits of answer of number raised to the power.
    """
    num = 2 ** 1000
    sums = 0
    while num > 0:
        temp = num % 10
        sums +=temp
        num//=10
    print(sums)
if __name__ == "__main__":
    main()
