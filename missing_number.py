'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

*** 
Solution:
The solution below uses a math trick to:
1. calculate the sum of numbers from 1 to n
2. find the sum of the input array 
The missing number is the difference between the 1st sum and the 2nd sum. 
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int((n * (n + 1))/2)
        sum_list = sum(nums)
        
        num_missing = total - sum_list
        return num_missin
 # Time complexity: O(N)
 # Space complexity: O(1)
        
