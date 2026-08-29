"""
Problem: Non-overlapping Intervals

Platform: LeetCode

Difficulty: Medium

Approach:

First, sort the intervals based on their ending times. This greedy ordering
helps keep the interval that finishes earliest, leaving the maximum possible
space for the remaining intervals.

Use a `visited` array to keep track of intervals that have already been removed.
Traverse the intervals and compare each interval with the later intervals using
the `isoverlap()` helper function. When two intervals overlap, remove the later
interval by marking it as visited and increment the removal count. Since the
intervals are sorted by their ending times, keeping the earlier interval is the
greedy choice because it leaves more room for future intervals.

The `isoverlap()` function checks whether two intervals overlap. Intervals that
only touch at their endpoints are considered non-overlapping.

Time Complexity: O(n²)

Space Complexity: O(n)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        visited = [False] * n
        res = 0

        for i in range(len(intervals) - 1):
            if visited[i]:
                continue

            for j in range(i + 1, len(intervals)):
                if visited[j]:
                    continue

                if self.isoverlap(intervals[i], intervals[j]):
                    visited[j] = True
                    res += 1

        return res

    def isoverlap(self, k, l):
        if k[0] < l[0]:
            if l[0] < k[1]:
                return True
            else:
                return False
        else:
            if k[0] < l[1]:
                return True
            else:
                return False