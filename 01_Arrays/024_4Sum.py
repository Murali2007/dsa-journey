"""
Problem: 4Sum

Platform: LeetCode

Difficulty: Medium

Approach:

First, sort the array so that duplicate values can be skipped efficiently and
the two-pointer technique can be applied. Iterate through the array using two
nested loops to fix the first and second elements of the quadruplet. Skip
duplicate values for both fixed elements to avoid generating repeated
quadruplets. For each pair, use two pointers—one starting just after the second
element and the other at the end of the array. Compute the sum of the four
elements. If the sum is smaller than the target, move the left pointer to
increase the sum. If it is larger, move the right pointer to decrease the sum.
When the sum equals the target, store the quadruplet, move both pointers, and
skip any duplicate values to ensure only unique quadruplets are included in the
result.

Time Complexity: O(n³)

Space Complexity: O(1)
(Excluding the space required for the output list)
"""
class Solution(object):
    def fourSum(self, arr, target):
        arr.sort()
        l = []

        for i in range(len(arr) - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, len(arr) - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                left = j + 1
                right = len(arr) - 1

                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        l.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1

                        while left < right and arr[left] == arr[left - 1]:
                            left += 1

                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return l