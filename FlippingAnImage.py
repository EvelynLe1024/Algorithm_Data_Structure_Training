'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image. 
To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in 
[0, 1, 1]. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results 
in [1, 0, 0].

Example 1:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

***
Solution:
The solution below (1) reverses each row of the matrix by turning each row into a reversed copy of itself, and (2) replace 1's with 0's
and 0's with 1's in each row. 

'''
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:        
        for i in range(len(A)):
            A[i] = A[i][::-1]
        for ele in A:
            for k in range(len(A[0])):
                if ele[k] == 0:
                    ele[k] = 1
                else:
                    ele[k] = 0
        return A
