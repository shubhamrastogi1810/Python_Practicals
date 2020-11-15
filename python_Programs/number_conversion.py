a = int(input("Enter a decimal number "))
b = a  
frmt ='{:15}:{:}' 
def convert_binary(a):
    addr = 0
    f = 0
    add = 0
    if a == 0 or a == 1:
        print(frmt.format("Binary is",a))
    else:
        while a >=1:
            bi = a % 2
            addr = (addr * 10) + bi 
            if addr == 0:
                f+= 1
            a = a // 2

        while addr >=1:
            ai = addr % 10
            add = (add * 10) + ai 
            addr = addr // 10 
        if f != 0:
            while f >=1:
                add *= 10
                f -= 1
        print(frmt.format("Binary is",add))

def convert_octal(a):
    addr = 0
    f = 0
    add = 0
    if a <= 7:
        print(frmt.format("Octal is",a))
    else:
        while a >=1:
            bi = a % 8
            addr = (addr * 10) + bi
            if addr == 0:
                f+= 1
            a = a // 8
    
        while addr >=1:
            ai = addr % 10
            add = (add * 10) + ai
            addr = addr // 10

        if f != 0:
            while f >=1:
                add *= 10
                f -= 1
        print(frmt.format("Octal is",add))

def convert_hexadecimal(a):
    addr = 0
    if 0 <= a <= 9:
        print(frmt.format("Hexadecimal is",a))
    elif 10 <= a <=15:
        print(frmt.format("Hexadecimal is",chr(a+55)))
    else:
        stri = ''
        while a >=1:
            he = a % 16
            if 0<= he <= 9:
                stri = stri + str(he)
            elif 10 <= he <= 15:
                stri = stri + str(chr(he+55))
            a = a // 16
        print(frmt.format("Hexadecimal is",stri[::-1]))

convert_binary(b)
convert_octal(b)
convert_hexadecimal(b)
