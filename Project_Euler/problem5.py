"""
    This code computes the smallest evenly divisible number from 1 to 20.
"""
def main():
    """
    This program prints the smallest evenly divisible number of first 20 natural numbers.
    """

    num = 9699690
    # multiplied all prime numbers. [2,3,5,7,11,13,17,19]
    while True:
        flag = True
        for i in [4,8,9,12,15,16,18,20,9699690]:
        # checking for the remaining numbers including the prime product.
            if num % i != 0:
                flag = False
                break
        if flag is True:
            print(num)
            break
        num+=2 # all the numbers in the list are even

if __name__ == "__main__":
    main()
