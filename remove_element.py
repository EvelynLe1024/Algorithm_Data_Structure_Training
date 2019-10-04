'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Source: https://leetcode.com/problems/remove-element/

***
Solution:
The solution below uses two pointers i and j to group the elements in-place. 
- i points to the first element that's different from val. 
- j iterates throuhg the array to find elements that are different from val to swap with the element at i
Whenever j points to an element different from val, we swap the elements at i and j and increment the two pointers each by 1. 
If not, we keep incrementing j by 1 until it reaches the end of the input array. 

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        return i
    
    # Time complexity: O(N)
    # Space complexity: O(1)
