"""Problem: Maximum Sum Circular Subarray

Platform: LeetCode

Difficulty: Medium

Approach:

First, compute the maximum subarray sum using Kadane's Algorithm for the normal
(non-circular) case. If all elements are negative, return this value immediately.
Otherwise, calculate the total array sum and negate every element. Running Kadane's
Algorithm on the negated array yields the magnitude of the minimum subarray sum in
the original array. Subtracting this minimum subarray sum from the total array sum
gives the maximum circular subarray sum. Finally, return the larger of the normal
maximum subarray sum and the circular maximum subarray sum.

Time Complexity: O(n)

Space Complexity: O(1)"""
class Solution(object):
    def normMaxSum(self,arr):
        res = arr[0]
        maxEnding = arr[0]
        for i in range(1,len(arr)):
            maxEnding = max(arr[i],maxEnding + arr[i])
            res = max(res,maxEnding)
        return res

    def maxSubarraySumCircular(self, arr):
        normMax = self.normMaxSum(arr)

        if normMax < 0:
            return normMax
        
        arr_sum = 0
        for i in range(len(arr)):
            arr_sum += arr[i]
            arr[i] = -arr[i]

        circularSum = arr_sum + self.normMaxSum(arr)
        return max(circularSum,normMax)
        
            

        