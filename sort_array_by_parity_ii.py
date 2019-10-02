'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even. Sort the array so that 
whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even. You may return any answer array that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Source: https://leetcode.com/problems/sort-array-by-parity-ii/

***
Solution:
The solution below:
1. creates an empty array with the same length as the input array 
2. iterates through the input array to find even numbers and insert them into the even indices of the new array 
3. iterate again through the input array to find odd numbers and insert them into the odd indices of the new array
'''
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        N = len(A)
        ans = [None]*N
        
        t = 0 
        for x in A:
            if x % 2 == 0:
                ans[t] = x
                t += 2
        t = 1
        for x in A:
            if x % 2 == 1:
                ans[t] = x
                t += 2
        return ans
        
  # Time complexity: O(N)
  # Space complexity: O(N)
