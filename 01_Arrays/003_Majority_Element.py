"""
Problem: Majority Element in the array
Platform: LeetCode
Difficulty: Easy

Approach:
Traverse the array once, using the Boyer–Moore Voting Algorithm to maintain a candidate 
and its count, updating the candidate whenever the count becomes zero.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def majorityElement(self, arr):

        res = 0
        count = 1
        for i in range(1,len(arr)):

            if arr[res] == arr[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                res = i
                count = 1
        return arr[res] 
       


        
        