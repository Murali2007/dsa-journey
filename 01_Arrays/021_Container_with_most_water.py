"""
Problem: Container With Most Water

Platform: LeetCode

Difficulty: Medium

Approach:

Use two pointers, one at the beginning of the array and the other at the end,
representing the two sides of the container. At each step, calculate the area
formed by the two lines using the distance between the pointers as the width and
the shorter of the two heights as the container's height. Update the maximum
area found so far. To potentially obtain a larger area, move the pointer
pointing to the shorter line inward, since moving the taller line cannot
increase the height while the width always decreases. Continue until the two
pointers meet.

Time Complexity: O(n)

Space Complexity: O(1)
"""
class Solution(object):
    def maxArea(self, arr):
        left = 0
        right = len(arr) - 1

        ans = 0

        while left < right:
            width = right - left
            height = min(arr[left], arr[right])

            area = width * height
            ans = max(ans, area)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return ans