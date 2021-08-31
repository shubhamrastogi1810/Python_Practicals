"""
    This code computes the smallest evenly divisible number from 1 to 20.
"""
NUM = 2521
while True:
    FLAG = True
    for i in range(1,21):
        if NUM % i != 0:
            FLAG = False
            break
    if FLAG is True:
        print(NUM)
        break
    NUM+=1
