"""
    This code will compute sum of the digits of the 100!
"""
def main():
    """
    This function prints sum of the digits the 100!
    """
    # Finding the 100 Factorial.
    prod = 1
    for i in range(2,101):
        prod*=i

    # Adding the Digits of 100!.
    sums = 0
    while prod > 0:
        temp = prod % 10
        sums+=temp
        prod //=10
    print(sums)
if __name__ == "__main__":
    main()
