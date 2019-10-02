'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order. 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

***
Solution:
The solution below:
1. uses a dictionary to count the frequency of each character in array 1
2. iterates through array 2 and extends to array "L" all the elements that are both in array 2 and the above dicionary with the frequency 
corresponding to the values of the characters (keys) in the dictionary. 
3. appends the remaining characters from array 1 to another array called "X". 
4. return array "L" concatenated with the sorted array "X"

A dictionary is used since retrieving a key or the value of a key in a dictionary takes constant time O(1) compared to O(N) if an array 
is used. 

'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1 = len(arr1)
        n2 = len(arr2)
        dict1 = collections.Counter(arr1)
        L = []
        X = []
        for ele in arr2:
            e = [ele] * dict1[ele]
            L.extend(e)
    
        for x in arr1:
            if x not in L:
                X.append(x)
        return L + sorted(X)
