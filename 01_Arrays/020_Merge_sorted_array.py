"""
Problem: Merge Sorted Array

Platform: LeetCode

Difficulty: Easy

Approach:

Use two pointers to traverse the valid elements of both sorted arrays
simultaneously. Compare the current elements and copy the smaller one into an
auxiliary array, advancing the corresponding pointer. After one array is fully
processed, copy the remaining elements from the other array into the auxiliary
array. Finally, copy all elements from the auxiliary array back into `nums1`,
resulting in a single sorted array containing all elements from both arrays.

Time Complexity: O(m + n)

Space Complexity: O(m + n)
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr = [0 for i in range(m + n)]

        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                k += 1
                i += 1
            else:
                arr[k] = nums2[j]
                k += 1
                j += 1

        while i < m:
            arr[k] = nums1[i]
            k += 1
            i += 1

        while j < n:
            arr[k] = nums2[j]
            k += 1
            j += 1

        for i in range(len(arr)):
            nums1[i] = arr[i]

        return nums1