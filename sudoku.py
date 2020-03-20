import numpy as np

#Converted to numpy array
sudoku = np.array([[0, 0, 2, 0, 1, 5, 0, 7, 8],
                   [1, 8, 0, 0, 6, 3, 4, 0, 0],
                   [0, 0, 4, 0, 2, 0, 5, 6, 1],
                   [0, 9, 6, 0, 0, 7, 0, 3, 0],
                   [0, 1, 0, 3, 0, 6, 0, 0, 5],
                   [0, 0, 3, 2, 0, 4, 0, 9, 6],
                   [0, 3, 0, 0, 0, 0, 0, 0, 0],
                   [6, 4, 9, 8, 3, 0, 2, 0, 7],
                   [0, 0, 7, 0, 0, 0, 0, 1, 0]
                   ])

# test if a value on a specific place is possible with current data
def possible(sudoku,rov, col, val):
    if sudoku[rov][col] != 0:
        return False #Already filled
    if val in sudoku[rov]:
        return False #Value already in row
    for a in range(9):
        if sudoku[a][col] == val:
            return False #value already in column
    sqrov = int(int(rov) / 3) * 3
    sqcol = int(int(col) / 3) * 3
    for r in range(sqrov, sqrov + 3):
        for c in range(sqcol, sqcol + 3):
            if sudoku[r][c] == val:
                return False #value already in square
    return True  # Value possible

#solve a sudoku if possible, Fill out list
def solve_Sudoku(sudoku):
    for rov in range(0, 9):
        for col in range(0, 9):
            if sudoku[rov][col] == 0:
                for val in range(1, 10):
                    if possible(sudoku,rov, col, val):
                        sudoku[rov][col] = val
                        if solve_Sudoku(sudoku):
                            return True
                        sudoku[rov][col] = 0 #Backtrack
                return False #Solution failed, backtrack for next value
    return True

solve_Sudoku(sudoku)
print(sudoku)