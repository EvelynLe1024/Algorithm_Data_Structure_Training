'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Source: https://leetcode.com/problems/min-cost-climbing-stairs/

***
Solution:
The solution below uses dynamic programming to build an empty array that stores the minimum cost (MC) at each step calculated using
recursion. 

Base cases:
- The minimum cost (MC) at step 1 is the value at index 0 in the input array. 
- The MC at step 2 is the value at index 1 in the input array. 

It then iterates through the input array from 0 to length array. At each step, we can decide whether to add the minimum cost of the last
one step or the last two steps (picking the smaller on) and add the cost of that step to build the rest of the empty array. 
The minimum cost of steps is the smaller value of the last two steps. 

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = [0] * len(cost) 
        f[0] = cost[0]
        f[1] = cost[1]
       
        for i in range(2, len(cost)):
            f[i] = cost[i] + min(f[i - 1], f[i - 2])
        return min(f[len(cost) - 1], f[len(cost) - 2])
