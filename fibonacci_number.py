'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the
two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Source: https://leetcode.com/problems/fibonacci-number/

***
Solution: 
The solution below uses dynamic programming to:
1. store the previously calculated value at each Fibonacci number and
2. return the value at F(N)

This solution improves upon the recursion only approach. It avoids recalculating the value of each Fibonacci number at each recursion
call by using an empty array to store such value and access them when needed. 

'''
class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        
        F = [0] * (N + 1)
        F[0] = 0
        F[1] = 1
        
        for i in range(2, N + 1):
            F[i] = F[i - 1] + F[i - 2]
        return F[N]
        
 # Time complexity: O(N)
 # Space complexity: O(N)
        
