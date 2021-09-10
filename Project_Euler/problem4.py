"""
This program will print the largest pallindrome numbers of product of 2 3digit numbers.
"""
def main():
    """
    This functin prints the largest 3-digit pallindrome numbers.
    """
    for i in range(999,900,-1):
        flag = False
        for j in range(999,900,-1):
            temp = i * j
            ans = temp
            summ = ""
            while ans > 0:
                tmp = ans % 10
                summ += str(tmp)
                ans //= 10
            if int(summ) == temp:
                print(i * j)
                flag = True
                break
        if flag is True:
            break
if __name__ == "__main__":
    main()
