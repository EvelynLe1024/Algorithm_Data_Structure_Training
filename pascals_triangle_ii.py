'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Source: https://leetcode.com/problems/pascals-triangle-ii/

***
Solution:
The solution below uses recursion to caculate the empty cells in the triangle. It:
1. initializes a triangle where all cells have 1's as values. This takes care of the base cases where the first and last columns
and the first two rows have 1's as values. 
2. runs two for loops. The outer loops iterates through each row in the triangle starting at row 2. The inner loop iterates through
each column in a row. 
3. calculates the value of cell [i, j] by adding together the the values of (1) the cell 1 colum to the left and 1 row above AND 
() the cell in the same column but one row above. 
4. returns the array of values at row k

'''
class Solution:
    def getRow(self, k: int) -> List[int]:
        res = [[1] * (i + 1) for i in range(k + 1)]
        for i in range(2, k + 1):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[k]
        
    # Time complexity: O(N^2)
    # Space complexity: O(N)
        
