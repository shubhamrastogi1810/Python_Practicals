"""This program sorts 3 numbers such that values are in assigned in ascending order to x,y,z. """
# unscrambled code
# z = tmp
# y = min(y,z)
# tmp = max(x,y)
# y = tmp
# y = tmp
# x = min(x,y)
# tmp = max(y,z)
# tmp = max(x,y)
# x = min(x,y)
num_one = int(input("value of x "))
num_two = int(input("value of y "))
num_three = int(input("value of z"))
# arranged code

temp = max(num_one,num_two)
num_one = min(num_one,num_two)
num_two = temp
temp = max(num_two,num_three)
num_two = min(num_two,num_three)
num_three = temp
temp = max(num_one,num_two)
num_one = min(num_one,num_two)
num_two = temp
print("x :",num_one)
print("y :",num_two)
print("z :",num_three)
