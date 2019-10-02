'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element. Now given an M x N matrix, return True if 
and only if the matrix is Toeplitz.
 
Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

*** 
The solution below:
1. uses two for loops to look at each cell in the matrix starting from column 2 (index 1) and row 2 (index 1) 
2. returns False if the value of a particular cell is different from the one that's one column to the left and one row above
3. returns True if the condition above holds for all the cells iterated through in the matrix
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
        
 # Time complexity: O(R * C) where R and C are the numbers of rows and columns in the matrix
 # Space complexity: O(1)
                
