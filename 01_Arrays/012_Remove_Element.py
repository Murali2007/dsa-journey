"""
Problem: Remove Element

Platform: LeetCode

Difficulty: Easy

Approach:

Traverse the array and copy every element that is not equal to the given value
into an auxiliary list. After processing all elements, copy the contents of the
auxiliary list back into the beginning of the original array. The length of the
auxiliary list represents the number of remaining elements after all occurrences
of the specified value have been removed, which is returned as the final answer.

Time Complexity: O(n)

Space Complexity: O(n)
"""

class Solution(object):
    def removeElement(self, arr, val):
        l = []
        for i in range(len(arr)):
            if arr[i]!=val:
                l.append(arr[i])
        
        for i in range(len(l)):
            arr[i] = l[i]
        
        return len(l)