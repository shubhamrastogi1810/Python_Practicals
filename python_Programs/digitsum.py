""" calculate the sum of the given number """
num = int(input("Enter a number "))
ADD =0
while num > 0:
    a = num % 10
    ADD+=a
    num= num // 10
print("your digit sum is ",ADD)
