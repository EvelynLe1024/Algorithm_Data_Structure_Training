'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

***
Solution:
The solution below uses two pointers i and j to group the elements in-place. 
- i points to the first element that's not a duplicate. 
- j iterates through the array to find elements that are not duplicates.
Whenever nums[j] != nums[j + 1], we have found a unique element nums[j + 1], so overwrite the value of nums[i + 1] with nums[j + 1}
We increment both i and j by 1. Otherwise, we keep incrementing j by 1 until it reaches the end of the input array.

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums ) == 0: 
            return 0
        i = 0 
        j = 0
        while j < len(nums) - 1:
            if nums[j] != nums[j + 1]:
                nums[i + 1] = nums[j + 1]
                i += 1
                j += 1
            else: 
                j += 1
        return i + 1
  
  # Time complexity: O(N)
  # Space complexity: O(1)
    
