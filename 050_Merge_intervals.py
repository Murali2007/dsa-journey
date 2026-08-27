"""
Problem: Merge Intervals

Platform: LeetCode

Difficulty: Medium

Approach:

First, sort the intervals based on their starting values. Store the first
interval in the result list. Then traverse the remaining intervals and compare
each current interval with the last interval in the result. If the current
interval overlaps with the last interval, merge them by extending the ending
value to the maximum of both ending values. If there is no overlap, add the
current interval as a new interval to the result. Continue this process until
all intervals have been processed.

Time Complexity: O(n log n)

Space Complexity: O(n)
(For the result list; excluding the sorting implementation's internal space)
"""
class Solution:
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, n):
            curr = intervals[i]
            last = res[-1]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)

        return res