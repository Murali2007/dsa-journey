"""
Problem: Valid Perfect Square

Platform: LeetCode

Difficulty: Easy

Approach:

Use Binary Search to determine whether the given number is a perfect square.
Maintain a search range from 1 to the given number. At each step, compute the
middle value and calculate its square. If the square equals the given number,
return True immediately. If the square is greater than the given number, search
the left half by updating the high pointer. Otherwise, search the right half by
updating the low pointer. If the search completes without finding an exact
square, return False.

Time Complexity: O(log n)

Space Complexity: O(1)
"""
class Solution(object):
    def isPerfectSquare(self, num):
        low = 1
        high = num

        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid

            if sqr == num:
                return True

            elif sqr > num:
                high = mid - 1

            else:
                low = mid + 1

        return False