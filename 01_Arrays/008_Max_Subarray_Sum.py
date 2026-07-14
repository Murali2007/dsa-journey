"""Problem: Maximum Subarray

Platform: LeetCode

Difficulty: Medium

Approach:

Use Kadane's Algorithm to maintain the maximum subarray sum ending at the current index.
At each element, decide whether to extend the previous subarray or start a new subarray
from the current element. Simultaneously track the overall maximum subarray sum encountered
during the traversal. This greedy dynamic programming approach computes the answer in a
single pass.

Time Complexity: O(n)

Space Complexity: O(1)
"""

class Solution(object):
    def maxSubArray(self, arr):
        maxEnding = arr[0]
        res = arr[0]
        for i in range(1,len(arr)):
            maxEnding = max(maxEnding + arr[i],arr[i])
            res = max(res,maxEnding)
        
        return res