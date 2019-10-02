'''
You are given an array of strings words and a string chars. A string is good if it can be formed by characters from chars (each character 
can only be used once). Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Source: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

*** 
Solution:
The solution below uses dictionaries to solve this problem. It
1. counts the number of times (value) each chracter (key) appears in chars
2. iterates through every string in words, do step 1 for each string
3. increment variable "total" by the lend of a string if all of the values for each key in that string is greater than or equal to 1
but less than or equal to the values for each key in chars. Basically, we want to make sure that all the characters in that string
do no appear more than the frequecy of each chracter in chars. 

'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not words and not chars:
            return 0
        if not words or not chars:
            return 0
        total = 0
        dictC = collections.Counter(chars)
        for i in range(len(words)):
            dictI = collections.Counter(words[i])
            if all(1<= dictI[key] <= dictC[key] for key in dictI.keys()):
                total += len(words[i])
        return total
        
 # Time complexity: O(N)
 # Space complexity: O(N)
