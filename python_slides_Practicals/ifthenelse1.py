""" first exercise of the if else from slides """
while 1:
    a = int(input("Enter a Number to Check"))
    if a % 2 == 0:
        print("No is Even")
    else:
        print("No is Odd")
    abc = int(input("Continue?1/0"))
    if  abc == 0:
        break
