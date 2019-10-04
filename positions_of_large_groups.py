'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

***
Solution: 
The solution below uses two pointers i and j to find the start (i) and the end (j) of each large group. i starts at 0, and j iterates 
from 0 to the end of the list. If j is at the last index of the input array or if the element at j is different from the element at (j + 1),
we compute the length from i to j to see if it's equal to or bigger than 3. If it is, we add [i, j] to the result array. We then move i to 
j + 1 where the element is different from the previous one. 

'''
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    res.append([i, j])
                i = j + 1
        return res
        
   # Time complexity: O(N)
   # Space complexity: O(N)
