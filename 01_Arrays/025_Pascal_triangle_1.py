"""
Problem: Pascal's Triangle

Platform: LeetCode

Difficulty: Easy

Approach:

Construct Pascal's Triangle row by row. For each row, the first and last
elements are always 1. Every intermediate element is obtained by adding the two
adjacent elements from the previous row. Store each completed row in the result
list, and use it to generate the next row. Continue this process until the
required number of rows has been generated.

Time Complexity: O(numRows²)

Space Complexity: O(numRows²)
"""
class Solution(object):
    def generate(self, numRows):
        l = []

        for i in range(numRows):
            k = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    k.append(1)
                else:
                    k.append(l[-1][j - 1] + l[-1][j])

            l.append(k)

        return l