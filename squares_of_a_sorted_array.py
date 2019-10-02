'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Source: https://leetcode.com/problems/squares-of-a-sorted-array/

*** 
Solution:
The solution below (1) iterates through all elements in the array to square them and (2) sorted the new array with squared elements. 
'''

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        S = [];
        for i in range(0, len(A)):
            S.append(A[i] * A[i]);
        return sorted(S);
        
# Time complexity: O(NlogN)
# Space complexity: O(N)
