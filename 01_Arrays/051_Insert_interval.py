"""
Problem: Insert Interval

Platform: LeetCode

Difficulty: Medium

Approach:

Insert the new interval into the existing list of non-overlapping sorted
intervals while merging any overlapping intervals. First, handle the case where
the input list is empty. A helper function `isoverlap()` checks whether two
intervals overlap by comparing their starting and ending values.

Traverse the intervals from left to right. If the current interval overlaps
with the new interval, merge them by taking the minimum starting point and
maximum ending point. Then continue checking the following intervals and merge
every interval whose starting point is less than or equal to the current merged
ending point. Mark all merged intervals as visited and add the resulting merged
interval to `res`.

If an interval does not overlap with the new interval, add it directly to the
result. After the main traversal, append any intervals that were not visited.
If the new interval did not overlap with any existing interval, add it
separately. Finally, sort the result to restore the required interval order.

Time Complexity: O(n log n)

Space Complexity: O(n)

Note: The sorting at the end makes the overall complexity O(n log n).
"""
class Solution: 
    def insert(self, intervals , newInterval) : 
        n = len(intervals) 
        k = newInterval 
        visited = [False] * n 
        res = [] 
        m = False 
 
        if not intervals: 
            res.append(k) 
            return res 
 
        def isoverlap(l, k): 
            m = [l, k] 
            m.sort() 

            if m[1][0] <= m[0][1]: 
                return True 
            else: 
                return False 
         
        for i in range(n): 
            start = intervals[i][0] 
            end = intervals[i][1] 
            visited[i] = True 

            if isoverlap(intervals[i], k): 
                m = True 
                start = min(start, k[0]) 
                end = max(end, k[1]) 
 
                j = i + 1 
                while j < n and intervals[j][0] <= end: 
                    end = max(end, intervals[j][1]) 
                    visited[j] = True 
                    j += 1 

                res.append([start, end]) 
                break 
            else: 
                res.append(intervals[i]) 
 
        i = 0 
        while i < n: 
            if visited[i]: 
                i += 1 
                continue 

            res.append(intervals[i]) 
            i += 1 
 
        if m == False: 
            res.append(k) 
         
        res.sort() 

        return res