'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least 
twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

***
Solution:
The solution iterates through the input array to store the elements in the input array in a dictionary. If we encounter an element in the
input array that already exists in the dictionary, it means that the input array contains duplicates. Otherwise, it doesn't. 
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}        
        for num in nums:    
            if num in dic:
                return True            
            dic[num] = 1
        return False
    
    # Time complexity: O(N)
    # Space complexity: O(N)
