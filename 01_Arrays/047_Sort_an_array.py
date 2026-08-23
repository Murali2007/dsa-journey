"""
Problem: Sort an Array

Platform: LeetCode

Difficulty: Medium

Approach:

Use the Merge Sort algorithm to sort the array. First, recursively divide the
array into two halves until each subarray contains only one element. Then merge
the two sorted halves using the `Merge` function. During merging, compare the
elements from the left and right subarrays and place the smaller element back
into the original array. Continue merging the sorted subarrays until the entire
array is sorted.

The `MergeSort` function performs the recursive division, while the `Merge`
function combines two already sorted portions of the array. Finally,
`sortArray` starts the Merge Sort process on the complete array.

Time Complexity: O(n log n)

Space Complexity: O(n)
"""
class Solution:
    def Merge(self, arr, l, m, h):
        n1 = m - l + 1
        n2 = h - m

        left = []
        right = []

        for i in range(n1):
            left.append(arr[l + i])

        for j in range(n2):
            right.append(arr[m + 1 + j])

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1

        while i < n1:
            arr[k] = left[i]
            k += 1
            i += 1

        while j < n2:
            arr[k] = right[j]
            k += 1
            j += 1

    def MergeSort(self, arr, l, h):
        if l < h:
            mid = (l + h) // 2

            self.MergeSort(arr, l, mid)
            self.MergeSort(arr, mid + 1, h)

            self.Merge(arr, l, mid, h)

        return arr

    def sortArray(self, arr) :
        return self.MergeSort(arr, 0, len(arr) - 1)