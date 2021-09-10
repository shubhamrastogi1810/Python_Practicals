"""
    This code will find the largest prime factor for the following number.
"""
def main():
    """
    Function will find the largest prime factor for the number.
    """
    num = 600851475143
    def isprime(number):
        """
            This function will return bool value if input number is prime or not.
        """
        flag = True
        for i in range(2,int(number ** 0.5)+1):
            if number % i == 0:
                flag = False
                break
        return bool(flag)

    factors = []
    for temp in range(3,int(num**0.5)+1):
        if num % temp == 0:
            factors.append(temp)
    factors.reverse()
    for j in factors:
        if isprime(j):
            print(j)
            break
if __name__ == "__main__":
    main()
