"""
Problem: Move Zeroes

Platform: LeetCode

Difficulty: Easy

Approach:

Traverse the array from left to right. Whenever a zero is encountered, search
the remaining portion of the array for the next non-zero element. Once found,
swap the zero with that non-zero element so that all non-zero elements gradually
move toward the beginning of the array while the zeros are shifted toward the
end. Continue this process until the entire array has been processed.

Time Complexity: O(n²)

Space Complexity: O(1)
"""
class Solution(object):
    def moveZeroes(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] == 0:
                for j in range(i + 1, len(arr)):
                    if arr[j] != 0:
                        arr[i], arr[j] = arr[j], arr[i]
                        break