'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) 
which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Source: https://leetcode.com/problems/array-partition-i/

***
Solution:
The questions asks us to find the maximum sum by adding the minimum from each pair. We can observe that a maximum number is sacrificed in
each pair for the smaller number to be added to the sum. The smallest element needs to be paird with the next smallest element so that 
the bigger elements will be added to the sum. 

The solution below will: 

1. sort the array 
2. use a for loop and increment it by 2 to make a pair starting from index 0 and add the minimum from each to the maximum sum
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_sum = 0 
        for i in range(len(nums), 2):
            max += min(nums[i], nums[i + 1])
        return max_sum
        
# Time complexity: O(NlogN)
# Space complexity: O(1)
