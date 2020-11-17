""" formatting practice """
ages = [('Joe',9), ('Samantha',45), ('Methuselah',969)]
FRMT = '{:10} {:3}'
for (name,age) in ages:
    print(FRMT.format(name,age))
