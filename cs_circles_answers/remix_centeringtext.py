""" put the entered text in center """
f = open("../input_csCircles/centertext.in","r")
ofset = 0
for i in f:
    if i != "END":
        ofset += len(i)
        print(i)
    else:
        print(ofset)
f.close()        
