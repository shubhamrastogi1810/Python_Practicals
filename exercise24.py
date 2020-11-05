ages = [('Joe',9), ('Samantha',45), ('Methuselah',969)]
frmt = '{:10} {:3}'
for (name,age) in ages:
    print(frmt.format(name,age))

