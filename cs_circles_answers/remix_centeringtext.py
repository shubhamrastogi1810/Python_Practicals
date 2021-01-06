""" put the entered text in center """
f = open("../input_csCircles/centertext.in","r")

for i in f:
    if i == "g":
        print("hello",end='')
    else:
        print(i,end='')
f.close()
