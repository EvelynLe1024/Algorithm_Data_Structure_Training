'''
Problem:
Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to 
the farthest leaf node. Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/

***
Solution:
The solution below uses recursion to find the maximum depth at each node and return the maximum depth at the root node.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right) 
 # Time complexity: O(N) 
 # Space complexity: O(1)
