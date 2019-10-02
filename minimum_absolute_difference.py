'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr 

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Source: https://leetcode.com/problems/minimum-absolute-difference/

***
Solution:
The solution below:
1. sorts the input array 
2. iterates through the sorted array to find the minimum difference between two consecutive numbers called "mini." 
The reason is that the minimum absolute difference can't exist between two numbers that are not next to each other since there's aways 
another pair whose absolute difference is smaller. 
3. iterates through the sorted array again to append the pairs of numbers whose absolute difference is the same as mini to another
output array called "res." 

Side note: The problem above was first posted by LeetCode as part of a weekly LeetCode contest. I submitted the following solution
as a contest participant, and it got accepted. 

'''
class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        mini = float("inf") 
        res = []
        n = len(A)
        A.sort()
        
        for i in range(n - 1):
            mini = min(mini, A[i + 1] - A[i])
        
        for i in range(n - 1):
            if A[i + 1] - A[i] == mini:
                res.append([A[i], A[i + 1]])
        return res
        
 # Time complexity: O(NlogN)
 # Space complexity: O(N)
