""" reading lines and printing length of the words """
filename = input('File name? ')
data = open(filename, 'r')

N_LINES = 0
N_WORDS = 0
N_CHARS = 0

for line in data:
    N_LINES += 1

    words_in_line = len(line.split())
    N_WORDS += words_in_line

    N_CHARS += len(line)

data.close()
print(filename," lines ",N_LINES," words ",N_WORDS," chars ",N_CHARS)
