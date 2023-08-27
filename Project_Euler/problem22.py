fil = open('names.txt','r')
abc = fil.readline().strip()
abc = abc.strip('"')
a = abc.split('","')
a.sort()

#print(a)
count = 0
grand_sum = 0
for i in a:
    summ = 0
    for j in i:
        summ += int(ord(j))-64
    count += 1
    #print(count * summ )
    grand_sum +=(count * summ)
print(grand_sum)
