"""
    This code computes the smallest evenly divisible number from 1 to 20.
"""
NUM = 9699690
while True:
    FLAG = True
    for i in [4,8,9,12,15,16,18,20,9699690]:

        if NUM % i != 0:
            FLAG = False
            break
    if FLAG is True:
        print(NUM)
        break
    NUM+=2
