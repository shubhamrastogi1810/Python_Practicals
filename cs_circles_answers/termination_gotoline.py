""" This program function will return the index of line where it is present """
#eg. findline(['10 GOTO 20','20 END'],'10')
#Output is 0 as index of 10 is 0

lists = ['10 GOTO 20','15 GOTO 20','20 END']

def findline(prog, target):
    """ Function will return the index of the line where no. found"""
    index = 0
    for count,item in enumerate(prog):
        thelist = (item.split())
        if thelist[0] == target:
            index = count
    return index
indx = findline(lists,'20')
print(indx)
