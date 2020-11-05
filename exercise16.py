filename = input('File name? ')
data = open(filename, 'r')

n_lines = 0
n_words = 0
n_chars = 0

for line in data:
    n_lines += 1

    words_in_line = len(line.split())
    n_words += words_in_line

    n_chars += len(line)

data.close()
print(filename," lines ",n_lines," words ",n_words," chars ",n_chars)

