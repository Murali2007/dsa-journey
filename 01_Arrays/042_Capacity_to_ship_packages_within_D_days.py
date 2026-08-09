"""
Problem: Capacity To Ship Packages Within D Days

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search on the possible shipping capacities. The minimum possible
capacity is the maximum package weight because every package must fit on the
ship, while the maximum possible capacity is the sum of all package weights,
which allows all packages to be shipped in one day. For each candidate capacity,
simulate the shipment in the given order and calculate how many days are
required. Keep adding package weights until adding the next package would exceed
the current capacity; then start a new day. If the required number of days is
less than or equal to the given number of days, the capacity is sufficient, so
search for a smaller capacity. Otherwise, increase the capacity. When the
pointers converge, `low` represents the minimum capacity required.

Time Complexity: O(n log(sum(weights)))

Space Complexity: O(1)
"""
class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            h = 0
            i = 1
            s = weights[0]

            while i < len(weights):
                s += weights[i]

                if s == mid:
                    h += 1
                    i += 1
                    s = 0

                elif s > mid:
                    h += 1
                    s = 0

                else:
                    i += 1

            if s > 0:
                h += 1

            if h <= days:
                high = mid
            else:
                low = mid + 1

        return low