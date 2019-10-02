'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array. Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]

*** 
Solution:
The solution below uses a dictionary to store the elements of the input array as keys for quick access. It then iterates from 1 to n. 
If a number in an iteration can't be found in the dictionary, that number is appended to a result list which stores all the elements 
that are missing from the input array. 

'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        dict = {}   
        
        for num in nums:
            dict[num] = 1;                
        for i in range (1, len(nums) + 1):
            if i not in dict:
                res.append(i)
        return res
        
   # Time complexity: O(N)
   # Space complexity: O(N)
