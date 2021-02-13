"""This program will find most word occured in a  input poem."""
poem_list = []
while True:
    newline = input()
    if newline == "" or "###" in newline:
        break
    poem_list.extend(newline.lower().split())
new_info = {}
for i in poem_list:
    COUNT = 0
    for j in range(len(poem_list)):
        if i == poem_list[j]:
            COUNT += 1
    new_info[i] = COUNT
words = list(new_info.items())
MAXVAL = 0
KEYVAL = ""
for key,val in words:
    if val > MAXVAL:
        MAXVAL = val
        KEYVAL = key
print(KEYVAL)
