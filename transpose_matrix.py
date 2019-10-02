'''
Given a matrix A, return the transpose of A. The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row 
and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Source: https://leetcode.com/problems/transpose-matrix/

***
Solution:
The solution below:
1. creates a new empty array T
2. iterates through the length of colums in the original input array A
3. at each iteration, it takes the elements at the a particular index in each row, turn them into new rows using list comprehension, 
and appends them to the new matrix T. 
'''
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        T = []   
        if not A:
            return None
        for i in range(len(A[0])):
            e = [arr[i] for arr in A]            
            T.append(e)
        return T
            
