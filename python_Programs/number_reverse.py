""" python code to reverse a number """
num = int(input("Enter a number "))
F = 0
while num > 0:
    A = num % 10
    F = F*10 + A
    num = num // 10
print("reverse of number  is ",F)
