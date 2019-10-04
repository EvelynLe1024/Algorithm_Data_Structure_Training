'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

***
Solution
I present here two different solutions to this problem. 
'''

'''
I. Solution 1: Greedy 
The first solution uses the greedy algorithm to find the desired indices. The greedy althorithm computes a solution in steps. At each step,
the algorithm picks a locally optimum option. The solution takes advantage of the sortedness of the array to:
1. use a while loop with two pointers i and j to iterate through the array. Pointer i starts at index 0, and pointer j starts at the last 
index of the array. 
2. compute the sum of the elements at each pair of i and j, shrinking the subarray from one side or the other. 
- If the sum is equal to target, we return the two indices incremented by 1 since since they are not zero-based. 
- If the sum is greater than the target, the rightmost element cannot be added to another element to equal the target, so we decrement j 
by 1. 
- If the sume if less than the target, the leftmost element cannot be added to another element to equal the target, so we increment i by 1
'''
class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        i = 0 
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] == target:
                return [i + 1, j + 1]
            elif A[i] + A[j] > target:
                j -= 1
            else:
                i += 1
    # Time complexity: O(N)
    # Space complexity: O(1)
