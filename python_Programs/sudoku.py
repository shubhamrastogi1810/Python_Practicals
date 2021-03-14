"""This code will input a blank sudoku and will print the filled matrix using recursive function."""
arr = [[]*9]*9
filevar = open('input_sudoku.txt','r')
for i in range(9):
    for j in range(9):
        a = filevar.readline().split(' ')
        if a == ['']:
            break
        a[-1] = a[-1].strip()
        arr[j] = list(map(int,a))

def print_matrix(matrix):
    """This function will print the matrix."""
    for row in range(9):
        for col in range(9):
            print(matrix[row][col], end = " ")
        print()


def isvalid(matrix, row, col, num):
    """This function will check for a number that it is unique in its column, row and box."""
    for val in range(9):
        if matrix[row][val] == num:
            return False

    for val in range(9):
        if matrix[val][col] == num:
            return False

    startr = row - row % 3
    startc = col - col % 3
    for mrow in range(3):
        for mcol in range(3):
            if matrix[mrow + startr][mcol + startc] == num:
                return False
    return True


def solvesuduko(matrix, row, col):
    """This function will fill value in cell if empty, and verifies it using isvalid function."""
    if (row == 8 and col == 9):
        return True

    if col == 9:
        row += 1
        col = 0

    if matrix[row][col] > 0:
        return solvesuduko(matrix, row, col + 1)

    for num in range(1, 10):
        if isvalid(matrix, row, col, num):
            matrix[row][col] = num
            if solvesuduko(matrix, row, col + 1):
                return True
        matrix[row][col] = 0
    return False


if solvesuduko(arr, 0, 0):
    print_matrix(arr)
else:
    print(" no solution  exists ")
