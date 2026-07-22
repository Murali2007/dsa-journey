"""
Problem: Pascal's Triangle II

Platform: LeetCode

Difficulty: Easy

Approach:

Generate Pascal's Triangle row by row until the required row index is reached.
For each row, the first and last elements are always 1. Every intermediate
element is computed as the sum of the two adjacent elements from the previous
row. Store each generated row in a list, and after constructing all rows up to
the specified index, return the last row as the required answer.

Time Complexity: O(rowIndex²)

Space Complexity: O(rowIndex²)
"""
class Solution(object):
    def getRow(self, rowIndex):
        l = []

        for i in range(rowIndex + 1):
            k = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    k.append(1)
                else:
                    k.append(l[-1][j - 1] + l[-1][j])

            l.append(k)

        return l[-1]