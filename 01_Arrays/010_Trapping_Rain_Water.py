"""Problem: Trapping Rain Water

Platform: LeetCode

Difficulty: Hard

Approach:

Precompute the tallest bar to the left and right of every index using two auxiliary
arrays. The left maximum array stores the highest bar from the beginning up to each
index, while the right maximum array stores the highest bar from the end up to each
index. For every bar except the first and last, the amount of water trapped is the
difference between the smaller of the two maximum heights and the current bar height.
Summing these values over all indices gives the total trapped rainwater.

Time Complexity: O(n)

Space Complexity: O(n)
"""
class Solution(object):
    def trap(self, arr):
        lmax = [0 for i in range(len(arr))]
        rmax = [0 for i in range(len(arr))]

        lmax[0] = arr[0]
        for i in range(1,len(arr)):
            lmax[i] = max(arr[i],lmax[i-1])

        rmax[len(arr) - 1] = arr[len(arr) - 1]
        for i in range(len(arr)-2,-1,-1):
            rmax[i] = max(arr[i],rmax[i+1])

        res = 0
        for i in range(1,len(arr)-1):
            res += min(lmax[i],rmax[i]) - arr[i] 

        return res   