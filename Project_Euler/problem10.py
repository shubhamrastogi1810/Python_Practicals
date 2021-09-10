"""
    This code will print the summation of prime numbers below 2 million.
"""
def main():
    """This code prints sums of prime numbers below 2 million."""
    sums = 2
    for i in range(3,2000000,2):
        flag = False
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                flag = True
                break
        if flag is False:
            sums+=i
    print(sums)
if __name__ == "__main__":
    main()
