"""
Problem: Sqrt(x)

Platform: LeetCode

Difficulty: Easy

Approach:

Use Binary Search to find the integer square root of the given number. Maintain
a search range from 0 to x and repeatedly compute the middle value. Compare the
square of the middle value with the given number. If the square is equal to x,
return the middle value immediately. If it is smaller, store the middle value as
the current best answer and continue searching in the right half for a larger
possible square root. Otherwise, search in the left half. When the search
terminates, the stored answer represents the floor value of the square root.

Time Complexity: O(log x)

Space Complexity: O(1)
"""
class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            res = mid * mid

            if res == x:
                return mid
            elif res > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans