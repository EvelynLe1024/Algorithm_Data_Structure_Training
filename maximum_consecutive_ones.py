'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

***
I present two different solutions to this problem. 

I. Solution 1: Dynamic Programming
The 1st solution uses dynamic programming to store the maximum count of 1's at each index in the input array. It uses an extra array 
for storage. It then returns the maximum value in the storage array. 

II. Solution 2: While Loop
The 2nd solution uses a while loop to iterate through the input array. If the element at index i is 1, the "count" variable is incremented
by 1. If the element at index i is 0, "count" is reset to 0. An extra array is created to keep track of the values of count at each index. 
'''

# Solution 1: Dynamic Programming
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if nums[0] == 1:
            dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
        return max(dp)
    # Time complexity: O(N)
    # Space complexity: O(N)
    
    # Solution 2: While Loop    
    class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        if not nums:
            return 0         
        i = 0 
        count = 0       
        list = []
        while i < len(nums):
            if nums[i] == 1:
                count += 1                            
                list.append(count)                
                j += 1
            else:
                count = 0
                j += 1
        return max(list)
     # Time complexity: O(N)
     # Space complexity: O(N)
    
