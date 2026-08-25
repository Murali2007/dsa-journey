"""
Problem: Sort Colors

Platform: LeetCode

Difficulty: Medium

Approach:

Use the Insertion Sort algorithm to sort the array in-place. Start from the
second element and treat the elements before it as a sorted portion. Store the
current element as `key` and compare it with the elements in the sorted portion.
While an element is greater than the key, shift it one position to the right.
Insert the key into its correct position. Repeat this process until the entire
array is sorted.

Since the array contains only 0, 1, and 2, the final result is all 0s followed
by all 1s and then all 2s.

Time Complexity: O(n²)

Space Complexity: O(1)
"""
class Solution:
    def sortColors(self, arr) -> None:
        i = 1

        while i < len(arr):
            j = i - 1
            key = arr[i]

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
            i += 1

        return arr