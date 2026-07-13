"""
Problem: Rotate Array

Platform: LeetCode

Difficulty: Medium


Approach:

Reverse the first (n-d) elements, then reverse the last d elements, and finally reverse the
entire array to rotate it to the right by d positions using the reversal algorithm.


Time Complexity: O(n)

Space Complexity: O(1)

"""
class Solution(object):
    def rev(self,low,high,arr):
        while(low<high):
            arr[low],arr[high] = arr[high],arr[low]
            low += 1
            high -= 1

    def rotate(self,arr, d):
        n = len(arr)
        d = d % n

        self.rev(0,n-d-1,arr)
        self.rev(n-d,n-1,arr)
        self.rev(0,n-1,arr)

        return arr