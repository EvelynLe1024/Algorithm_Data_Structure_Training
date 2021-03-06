'''
Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the 
police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob 
tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
Source: https://leetcode.com/problems/house-robber/

****
Solution:
The solution below uses dynamic programming to store the maximum amount of money the robber could steal at each house given that he 
cannot steal from two adjacent houses in one night. The solution returns the maximum amount of money at the last index of the memoization
array.

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        h = [0] * n
        h[0] = nums[0] 
        h[1] = max(nums[1], nums[0])
    
        for i in range(2, n):
            h[i] = max(nums[i] + h[i - 2], h[i - 1])
        return h[n - 1]
      
 # Time complexity: O(N)
 # Space complexity: O(N)
 
