"""
Problem: Count of Smaller Numbers After Self

Platform: LeetCode

Difficulty: Medium

Approach:

The solution uses Merge Sort while keeping track of each element's original
index.

1. Create pairs `(value, index)` so that each number can be connected to its
   original position.
2. Initialize `counts` with zeros. `counts[i]` stores the number of elements
   smaller than `nums[i]` that appear to its right.
3. During Merge Sort, recursively divide the array into left and right halves.
4. While merging:
   - If the current left value is greater than the current right value, the
     right element is smaller and lies to the right of the left element.
   - Increment `right_count`.
   - When a left element is selected, add `right_count` to its count.
5. Merge the two sorted halves and continue the process.
6. Finally, return `self.counts`.

Key Idea:

During the merge step, `right_count` tells us how many elements from the
right half are smaller than the current element from the left half.

Because Merge Sort processes elements from different halves, we can count
smaller elements to the right efficiently instead of comparing every pair.

Time Complexity: O(n log n)

Space Complexity: O(n)

The Merge Sort recursion and temporary arrays require additional space.
"""

class Solution:
    def __init__(self):
        self.count = []

    def countSmaller(self, nums):
        k = []
        self.counts = [0] * len(nums)

        for i in range(len(nums)):
            k.append((nums[i], i))

        self.Mergesort(k)
        return self.counts

    def Mergesort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_arr = self.Mergesort(nums[:mid])
        right_arr = self.Mergesort(nums[mid:])

        return self.Merge(left_arr, right_arr)

    def Merge(self, l, r):
        i = 0
        j = 0
        right_count = 0

        while i < len(l) and j < len(r):
            if l[i][0] > r[j][0]:
                right_count += 1
                j += 1
            else:
                self.counts[l[i][1]] += right_count
                i += 1

        while i < len(l):
            self.counts[l[i][1]] += right_count
            i += 1

        i = 0
        j = 0
        k = []

        while i < len(l) and j < len(r):
            if l[i][0] <= r[j][0]:
                k.append(l[i])
                i += 1
            else:
                k.append(r[j])
                j += 1

        return k + l[i:] + r[j:]