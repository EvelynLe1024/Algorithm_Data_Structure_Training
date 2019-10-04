'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Source: https://leetcode.com/problems/search-a-2d-matrix/

*** 
Solution:
The solution below uses binary search to (1) find the two rows that might contain the target, and (2) find the target in each of the row.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		# Edge cases: if the matrix is empty or if the matrix is not empty but has an empty element, return False.
        if not matrix or not matrix[0]:  
            return False
        
		# Helper function to narrow down the array to two elements at indices 'hi' and 'lo' that might equal the target value
        def biSearch(arr, tar):
            lo, hi = 0, len(arr) - 1
            while lo + 1 < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] > tar:
                    hi = mid
                else:
                    lo = mid
            return arr[hi] == tar or arr[lo] == tar                
       
	   # The main function narrows the matrix down to two rows at indices 'hi' and 'lo' that might have the target value. We compare the first value of each 
	   # rows to the target value. If the 1st element of the row at 'hi' is greater than the target, it means that we need to search for the target in the 
	   # row at 'lo', and vice versa.
	   
        loR, hiR = 0, len(matrix) - 1
        while loR + 1 < hiR:
            mid = loR + (hiR - loR) // 2
            if matrix[mid][0] > target:
                hiR = mid
            else:
                loR = mid
        if matrix[hiR][0] > target:
            return biSearch(matrix[loR], target)
        else:
            return biSearch(matrix[hiR], target)   
