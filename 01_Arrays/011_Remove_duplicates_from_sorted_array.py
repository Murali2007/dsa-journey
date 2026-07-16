"""
Problem: Remove Duplicates from Sorted Array

Platform: LeetCode

Difficulty: Easy

Approach:

Since the array is already sorted, all duplicate elements appear consecutively.
Create an auxiliary list and add the first element to it. Traverse the array from
the second element onward, and whenever the current element differs from the
previous one, append it to the auxiliary list. After collecting all unique
elements, copy them back into the beginning of the original array. Finally,
return the number of unique elements.

Time Complexity: O(n)

Space Complexity: O(n)
"""

class Solution(object):
    def removeDuplicates(self, arr):
        l = []
        l.append(arr[0])
        for i in range(1,len(arr)):
            if arr[i] != arr[i-1]:
                l.append(arr[i])
        for i in range(len(l)):
            arr[i] = l[i]
        return len(l)