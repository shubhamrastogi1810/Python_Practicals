""" This program will read the list until it reaches the END in the string """
# This will determine the string termination(When to terminate strings)
# 10 GOTO 20
# 20 END
# This will return these 2 lines as 2 line endswith END.

def getbasic():
    """ This function returns list of the input until END found """
    newlis = []
    while 1:
        strin = input()
        char = strin.split(" ")
        newlis.append(strin)
        if char[-1] == "END":
            break
    return newlis
ret_list = getbasic()
print(ret_list)
