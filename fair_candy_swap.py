'''
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the 
j-th bar of candy that Bob has. Since they are friends, they would like to exchange one candy bar each so that after the exchange, 
they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar 
that Bob must exchange. If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

Example 1:
Input: A = [1,1], B = [2,2]
Output: [1,2]

Source: https://leetcode.com/problems/fair-candy-swap/

***
The strategy here is that Alice will need to give Bob an amount of candy that makes up for the difference between Alice's or Bob's amount
and the average candy of the two. 

The solution below:
1. finds the average amount of candy each person can have
2. finds the difference between Alice's amount of candy and the average
3. uses a dictionary to store all the candies Bob has as keys
4. checks if Bob has an amount of candy he can give to Alice can increase her candy amount to the average of the two

'''
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        mid = (sum(A) + sum(B))/2
        dif = mid - sum(A)
        dic = {}
        
        for candyB in B:
            dic[candyB] = 1
            
        for candyA in A:
            if int(candyA + dif) in dic:
                return [candyA, int(candyA + dif)]
                
  # Time complexity: O(N)
  # Space complexity: O(N)
       
