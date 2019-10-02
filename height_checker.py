'''
Students are asked to stand in non-decreasing order of heights for an annual photo. Return the minimum number of students not standing in 
the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of 
height.)

Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.

Source: https://leetcode.com/problems/height-checker/
****

Solution:
The solution below creates a new list that is the sorted version of the input array. It then iterates through the original input array 
and compares the elements at the same indices in the two arrays. Everytime two elements at the same index are different, the variable
"count" is incremted by 1. 
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights);
        count = 0;
        for i in range(len(heights)):
            if heights[i] != sorted_list[i]:
                count += 1
        return count
        
 # Time complexity: O(NlogN)
 # Space complexity: O(N)
