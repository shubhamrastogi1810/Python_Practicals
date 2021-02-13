""" This program inputs 1) time in a 24-hour clock 2) time to add in minutes, and prints new time"""
# time is 12 : 47
# add minutes :-  15
# output should be :- 13:02
time = input("Enter the time ")
addminute = int(input("Enter the minutes to add "))
HOUR,minute = map(int,time.split(":"))
FRMT ='{:02d}:{:02d}'
newmin = minute + addminute#M

if newmin > 60:
    newhour = newmin // 60
    if (HOUR+ newhour)>= 24 and newhour <=23:
        newhour = (newhour + HOUR) - 24
        newmin = newmin - (newhour +(24-HOUR))*60
    elif newhour == 1 and HOUR == 23:
        HOUR = 0
        newmin = newmin - newhour * 60
    elif HOUR == 23 and newhour > 1:
        HOUR = 0
        newhour = (newmin // 60) - 1
        if newhour >= 24:
            newhour = newhour - 24
            newmin = newmin - (newhour + 25) * 60
        else:
            newmin = newmin - (newmin // 60 ) * 60
    else:
        newmin = newmin - newhour * 60
        newhour = HOUR + newhour


print(FRMT.format(newhour,newmin))
