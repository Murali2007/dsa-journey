"""
Problem: 3Sum

Platform: LeetCode

Difficulty: Medium

Approach:

First, sort the array so that duplicate values can be skipped efficiently and
the two-pointer technique can be applied. Iterate through the array, treating
each element as the first number of a potential triplet. For every selected
element, use two pointers—one starting from the next index and the other from
the end of the array. If the sum of the three elements is less than zero, move
the left pointer to increase the sum. If the sum is greater than zero, move the
right pointer to decrease the sum. When the sum equals zero, store the triplet,
move both pointers, and skip any duplicate values to ensure only unique triplets
are included in the result.

Time Complexity: O(n²)

Space Complexity: O(1)
(Excluding the space required for the output list)
"""
class Solution(object):
    def threeSum(self, arr):
        arr.sort()
        n = len(arr)
        l = []

        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    l.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

        return l