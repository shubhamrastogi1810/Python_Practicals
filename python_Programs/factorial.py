""" to find a factorial of a number """
no = int(input("Enter a number "))
F = 1
while no > 1:
    F*=no
    no-=1
print("factorial no is ",F)
