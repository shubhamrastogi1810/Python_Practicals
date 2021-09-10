"""
    This program calculates the 10001th prime number.
"""
def main():
    """
    This function prints 10001st prime number.
    """
    lis = [2,3]
    num = 5
    while len(lis) != 10001:
        flag = True
        for j in range(2,int(num**0.5)+1):
            if num % j == 0:
                flag = False
                break
        if flag is True:
            lis.append(num)
        num+=2
    print(lis[-1])

if __name__ == "__main__":
    main()
