""" reading data and finding the  chars, words, lines of the file """
filename = input('File name? ')
data = open(filename, 'r')



def file_stats(data):
    """ reading data and printing the lines, chars, words from the file """
    n_lines = 0
    n_words = 0
    n_chars = 0

    for line in data:
        n_lines += 1
        line_words = line.split()
        n_words += len(line_words)
        n_chars += len(line)

    return n_lines,n_words, n_chars


print(filename,file_stats(data))
data.close()
