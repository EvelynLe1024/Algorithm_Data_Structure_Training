'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Source: https://leetcode.com/problems/sort-array-by-parity/

*** 
Solution:
The solution below uses (1) pointer "even" as an index that starts at index 0 of the list, (2) a for loop to iterate through the list and 
swap any even element at index i with the element at index "even" and then increment "even" by 1. This method sorts the array in-place. 

Approach approach to sorting the list is create an empty list and iterate through the array twice to 1) first append the even elements and
2) append the odd elements. This approach is less efficient than the first one, however, since it uses extra space. 

'''
# Approach 1: in-place sorting
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) < 1 and len(A) > 5000:
            return None
            
        even = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[even], A[i] = A[i], A[even]
                even += 1
        return A
        
  # Approach 2: Creating an additional array
  class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) < 1 and len(A) > 5000:
            return None
       
        new_list = []        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                new_list.append(A[i])                 
        for j in range(len(A)):
            if A[j] % 2 == 1:
                new_list.append(A[j])
        return new_list
      
