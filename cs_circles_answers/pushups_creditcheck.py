""" This program checks that the credit card is valid or not based on the following criteria"""
# String should follow the format "#### #### #### ####", and here all '#' represents
# a digit. and Through checksum method if sum of all digits is divisible by 10 then
# return True else False.
FRMT = '{:21}:{:}'
def check(string):
    """ This function inputs card number and returns True/False after checking certain conditions"""
    if string != "" and len(string) == 19:
        if string[4]==" " and string[9]==" " and string[14]==" ":
            temp = add = 0
            for i in string:
                if 48 <= ord(i) <= 57 or ord(i) == 32:
                    temp = 1
                    if 48 <= ord(i) <= 57:
                        add += int(i)
                else:
                    temp = 0
                    break
            if temp == 1:
                return bool(add % 10 == 0 and add!= 0)
            else:
                return False
        else:
            return False
    else:
        return False
print(FRMT.format('0000 000000000000',check('2768 3424 2345 2358')))
print(FRMT.format('9384 3495 3297 0121',check('9384 3495 3297 0121')))
print(FRMT.format('0000000000000000',check('0000000000000000')))
print(FRMT.format('1876 0954 325009182',check('1876 0954 325009182')))
print(FRMT.format(' 5555 5555 5555 5555',check(' 5555 5555 5555 5555')))
print(FRMT.format('0000 0000 0000 000',check('0000 0000 0000 000')))
print(FRMT.format('0 0 0 0000000000000',check('0 0 0 0000000000000')))
print(FRMT.format('\'\'',check('')))
print(FRMT.format('0000 0000',check('0000 0000')))
print(FRMT.format('0123 4567 8902 4568',check('0123 4567 8902 4568')))
print(FRMT.format('0123 4567 89AB EFGH',check('0123 4567 89AB EFGH')))
print(FRMT.format('0000 000000000000',check('0000 000000000000')))
