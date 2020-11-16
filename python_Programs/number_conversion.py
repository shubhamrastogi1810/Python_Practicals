""" This program is to convert a decimal into hexamdecimal, octal, and binary """
num_inp = int(input("Enter a decimal number "))
FRMT ='{:15}:{:}'
def convert_binary(number):
    """ This  function is used to convert decimal to binary """
    rev_bin = 0
    count = 0
    bin_num = 0
    if number in (0,1):
        print(FRMT.format("Binary is",number))
    else:
        while number >=1:
            num_rem = number % 2
            rev_bin = (rev_bin * 10) + num_rem
            if rev_bin == 0:
                count+= 1
            number //= 2

        while rev_bin >=1:
            div_bin = rev_bin % 10
            bin_num = (bin_num * 10) + div_bin
            rev_bin //= 10
        if count != 0:
            while count >=1:
                bin_num *= 10
                count -= 1
        print(FRMT.format("Binary is",bin_num))

def convert_octal(number):
    """ This  function is used to convert decimal to octal """
    rev_oct = 0
    count = 0
    oct_num = 0
    if num_inp <= 7:
        print(FRMT.format("Octal is",number))
    else:
        while number >=1:
            div_rem = number % 8
            rev_oct = (rev_oct * 10) + div_rem
            if rev_oct == 0:
                count+= 1
            number //= 8
        while rev_oct >=1:
            oct_rem = rev_oct % 10
            oct_num = (oct_num * 10) + oct_rem
            rev_oct = rev_oct // 10

        if count != 0:
            while count >=1:
                oct_num *= 10
                count -= 1
        print(FRMT.format("Octal is",oct_num))

def convert_hexadecimal(number):
    """ This  function is used to convert decimal to hexadecimal """
    if 0 <= number <= 9:
        print(FRMT.format("Hexadecimal is",number))
    elif 10 <= number <=15:
        print(FRMT.format("Hexadecimal is",chr(number+55)))
    else:
        strin = ''
        while number >=1:
            hex_rem = number % 16
            if 0<= hex_rem <= 9:
                strin = strin + str(hex_rem)
            elif 10 <= hex_rem <= 15:
                strin = strin + str(chr(hex_rem+55))
            number //= 16
        print(FRMT.format("Hexadecimal is",strin[::-1]))

convert_binary(num_inp)
convert_octal(num_inp)
convert_hexadecimal(num_inp)
