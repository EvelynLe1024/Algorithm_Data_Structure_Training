'''
An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, 
A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

***
The solution below compares the input array with its sorted version in (1) ascending order if the first two elements are in the same order
or (2) descending order otherwise. 

'''
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        if A[0] >= A[1]:
            return A == sorted(A, reverse=True)
        else:
            return A == sorted(A)
    
            
   # Time complexity: O(NlogN)
   # Space complexity: O(1)
