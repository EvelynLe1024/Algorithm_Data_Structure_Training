'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Source: https://leetcode.com/problems/majority-element/

*** 
Solution:
The solution below uses a hashtable to store the values that appear in the array as keys and their frequency as values. It then iterates
through the keys in the hashtable to find the key with the counts larger than n/2.

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for key in dict:
            if dict[key] > n/2:
                return key                
 # Time complexity: O(N)
 # Space complexity: O(N)
