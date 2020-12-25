""" This program is used to add minutes in the input time """
# time is 12 : 47
# add minutes -  15
# output should be - 13:02
time = input("Enter the time ")
addminute = int(input("Enter the minutes to add "))
hour,minute = map(int,time.split(":"))
FRMT ='{:02d}:{:02d}'
newmin = minute + addminute#M

if newmin > 60:
    newhour = newmin // 60
    if (hour+ newhour)>= 24 and newhour <=23:
        newhour = (newhour + hour) - 24
        newmin = newmin - (newhour +(24-hour))*60
    elif newhour == 1 and hour == 23:
        hour = 0
        newmin = newmin - newhour * 60
    elif hour == 23 and newhour > 1:
        hour = 0
        newhour = (newmin // 60) - 1
        if newhour >= 24:
            newhour = newhour - 24
            newmin = newmin - (newhour + 25) * 60
        else:
            newmin = newmin - (newmin // 60 ) * 60
    else:
        newmin = newmin - newhour * 60
        newhour = hour + newhour


print(FRMT.format(newhour,newmin))
