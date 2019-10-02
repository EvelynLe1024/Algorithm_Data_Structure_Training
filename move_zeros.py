'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Source: https://leetcode.com/problems/move-zeroes/

*** 
Solution:
The solution below uses two pointers i and j that are initialized to 0 to modify the array in-place. It uses a while loop to iterate 
through the input array. i points to the first index in the array that hasn't been modified. j iterates through the list to find
elements that are different from 0 to swap with i. Whenever an element at j is different from 0, we swap the two elements at i and j 
and increment both pointers by 1. If an element is 0, j is incremented by 1. 

'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j = 0
        n = len(nums)
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]                
                i += 1
                j += 1
            else: 
                j += 1
                
  # Time complexity: O(N)
  # Space complexity: O(1)
        
