# Sudoku_Puzzle-
Solving Sudoku puzzle using both Recursion and Backtracking

This sample is inspired by a video from the Youtube channel Computerfile.
https://www.youtube.com/watch?v=G_UYXzGuqvM&feature=youtu.be

Here is a typically **Sudoku**, let's solve that.

In this sample, the exiting things is happening in the **“Solve”** function.

The **“possible”** function just checks any value for obeying the sacred rules of Sudoku.

You know:

- Only values between 1 and 9 can be used
- Only one occurrence of a value in each row
- Only one occurrence of a value in each column
- Only one occurrence of each value in one square when the sudoku plate is divided into nine squares

The **“solve”** function iterates through each row and each column in the sudoku array, looking for an unsolved field (containing 0). When found, it's iterating through possible values. Trying each value with the **“Possible”** function, until “possible” return **True.**

If the **“Possible”** function returns true, the value is kept in the sudoku array, and the **“Solve”** function is recursively called to iterate to the next Row/column with unsolved value. This is illustrated with green arrows below.
![Function calls](C:\Users\Hp pavilion\Downloads\sudokufunctionCall.png)

Maybe not the best illustration in the world, but making it helped me understand the whole thing better, which is the main point of this article.

If the “possible” function returns False, the sudoku array field is marked unsolved again, and the loop looks for the next value to try in the field. If no value for a field could fulfill the rules of sudoku, the backtracking begins.

The red arrow in the illustration show that a False result from the possible function resolves in the value in the sudoku array is erased (backtracked), and the loop continues to the next value. This backtracking can go multiple steps backwards until the “possible” function starts returning True again. Then the recursion moves forward shown with green arrows.
![Function calls](C:\Users\Hp pavilion\Downloads\sudokufunctionCall1.png)

When the row and col loop reach the end, the sudoku is solved if possible, and “solve” function returns true all the way through the call stack, until it reaches the entry point. The blue arrows.

![Function calls](C:\Users\Hp pavilion\Downloads\sudokufunctionCall2.png)

The solved sudoku is printed.

[[9 6 2 4 1 5 3 7 8]
 [1 8 5 7 6 3 4 2 9]
 [3 7 4 9 2 8 5 6 1]
 [4 9 6 1 5 7 8 3 2]
 [2 1 8 3 9 6 7 4 5]
 [7 5 3 2 8 4 1 9 6]
 [5 3 1 6 7 2 9 8 4]
 [6 4 9 8 3 1 2 5 7]
 [8 2 7 5 4 9 6 1 3]]
