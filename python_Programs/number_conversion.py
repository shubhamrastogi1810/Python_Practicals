a = int(input("Enter a number "))
b = a  
def convert_binary(a):
	addr = 0
	f = 0
	add = 0
	if a == 0 or a == 1:
		print("Binary is: ",a)
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
		print("Binary is: ",add)

def convert_octal(a):
        addr = 0
        f = 0
        add = 0
        if a <= 7:
                print("Octal is: ",a)
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
                print("Octal is: ",add)

convert_binary(b)
convert_octal(b)
