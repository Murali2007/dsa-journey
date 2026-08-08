"""
Problem: Koko Eating Bananas

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search on the possible eating speeds. The minimum possible speed is
1 and the maximum possible speed is the largest pile. For each candidate speed,
calculate the total number of hours required to finish all banana piles. The
ceiling division `(piles[i] + mid - 1) // mid` gives the hours needed for each
pile. If the total hours are less than or equal to the allowed hours, the
current speed is sufficient, so search for a smaller speed by moving the high
pointer to `mid`. Otherwise, the speed is too slow, so search the right half by
moving the low pointer to `mid + 1`. When both pointers converge, `low` is the
minimum eating speed that allows all bananas to be eaten within the given time.

Time Complexity: O(n log(max(piles)))

Space Complexity: O(1)
"""
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            k = 0
            for i in range(len(piles)):
                k += (piles[i] + mid - 1) // mid

            if k <= h:
                high = mid
            else:
                low = mid + 1

        return low