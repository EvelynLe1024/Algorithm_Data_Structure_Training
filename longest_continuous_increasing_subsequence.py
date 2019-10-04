'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence LIS) (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Source: https://leetcode.com/problems/longest-continuous-increasing-subsequence/

*** 
Solution:
The solution below uses a for loop to interate through the array. If a subarray is increasing, it will increment count by 1 and update the
maximum length of the LIS subarray. If the subarray is decreasing, count is reset to 1. 

'''
class Solution:
    def findLengthOfLCIS(self, A: List[int]) -> int:
        if not A:
            return 0
        
        total = 1 
        count = 1
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                count += 1                
                total = max(total, count)
            else:
                count = 1
        return total
        
   # Time complexity: O(N)
   # Space complexity: O(1)
