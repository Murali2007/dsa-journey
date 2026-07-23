"""
Problem: Third Maximum Number

Platform: LeetCode

Difficulty: Easy

Approach:

Maintain three variables to store the first, second, and third largest distinct
elements encountered while traversing the array. Ignore duplicate values to
ensure only distinct numbers are considered. For each element, update the three
maximum values by shifting the existing values whenever a larger element is
found. After processing the entire array, return the third maximum if it exists;
otherwise, return the largest element.

Time Complexity: O(n)

Space Complexity: O(1)
"""
class Solution(object):
    def thirdMax(self, arr):
        first = second = third = None

        for num in arr:
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num

            elif second is None or num > second:
                third = second
                second = num

            elif third is None or num > third:
                third = num

        return first if third is None else third