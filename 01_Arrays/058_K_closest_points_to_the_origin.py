"""
Problem: K Closest Points to Origin

Platform: LeetCode

Difficulty: Medium

Approach:

Calculate the distance of every point from the origin using the Euclidean
distance formula. Store these distances in a separate list while keeping the
corresponding points at the same indices.

Use Merge Sort to sort the distances in ascending order. During the merge
process, whenever a distance from the left half is smaller than or equal to a
distance from the right half, add the left distance and its corresponding point
to the merged lists. Otherwise, add the right distance and its corresponding
point. This keeps the points synchronized with their distances while sorting.

After sorting all points based on their distance from the origin, take the first
`k` points and return them.

Time Complexity: O(n log n)

Space Complexity: O(n log n)

where `n` is the number of points. The Merge Sort implementation creates
additional lists during recursive splitting and merging.
"""
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []

        for point in points:
            val = math.sqrt(point[0] * point[0] + point[1] * point[1])
            l.append(val)

        l, points = self.Mergesort(l, points)

        res = []

        for i in range(k):
            res.append(points[i])

        return res

    def Mergesort(self, l, points):
        if len(l) <= 1:
            return l, points

        mid = len(l) // 2

        left_arr = self.Mergesort(l[:mid], points[:mid])
        right_arr = self.Mergesort(l[mid:], points[mid:])

        return self.Merge(
            left_arr[0],
            right_arr[0],
            left_arr[1],
            right_arr[1]
        )

    def Merge(self, l, r, l1, r1):
        k = []
        m = []

        i = 0
        j = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                k.append(l[i])
                m.append(l1[i])
                i += 1
            else:
                k.append(r[j])
                m.append(r1[j])
                j += 1

        return k + l[i:] + r[j:], m + l1[i:] + r1[j:]