"""
Problem: Minimum Number of Arrows to Burst Balloons

Platform: LeetCode

Difficulty: Medium

Approach:

Sort the balloons by their ending points. Start by placing the first arrow at
the end position of the first balloon. This arrow can burst every following
balloon whose starting point is less than or equal to the arrow position.

Traverse the remaining balloons. If the current balloon starts after the
current arrow position, it cannot be burst by the existing arrow, so a new
arrow is required. Place the new arrow at the current balloon's ending point.
If the current balloon starts at or before the arrow position, it overlaps with
the arrow's position and can be burst by the same arrow.

Because the intervals are sorted by their ending points, always placing an
arrow at the earliest possible ending point is the greedy choice.

Time Complexity: O(n log n)

Space Complexity: O(1)
(Excluding the space used internally by the sorting algorithm)
"""
class Solution:
    def findMinArrowShots(self, arr) -> int:
        arr.sort(key=lambda x: x[1])
        n = len(arr)

        arrows = 1
        pos = arr[0][1]

        for i in range(1, len(arr)):
            if arr[i][0] > pos:
                arrows += 1
                pos = arr[i][1]

        return arrows