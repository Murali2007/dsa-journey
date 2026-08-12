"""
Problem: Minimum Number of Days to Make m Bouquets

Platform: LeetCode

Difficulty: Medium

Approach:

Use Binary Search on the number of days required to make the bouquets. The
minimum possible day is 1 and the maximum possible day is the largest value in
`bloomDay`. For each candidate day, traverse the array and count consecutive
flowers that have bloomed by that day. Whenever `k` consecutive bloomed flowers
are found, form one bouquet and reset the consecutive flower count. If the
number of bouquets formed is at least `m`, the candidate day is sufficient, so
search for a smaller number of days. Otherwise, increase the number of days.
Before applying Binary Search, check whether there are enough flowers in total
to make all required bouquets.

Time Complexity: O(n log(max(bloomDay)))

Space Complexity: O(1)
"""
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1

        low = 1
        high = max(bloomDay)

        while low < high:
            mid = (low + high) // 2

            c = 0
            bouquets = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    c += 1
                else:
                    c = 0

                if c == k:
                    bouquets += 1
                    c = 0

            if bouquets >= m:
                high = mid
            else:
                low = mid + 1

        return low