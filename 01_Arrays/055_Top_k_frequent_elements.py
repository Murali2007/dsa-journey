"""
        Problem: Top K Frequent Elements

        Platform: LeetCode

        Difficulty: Medium

        Approach:

        Use a dictionary to count the frequency of every element in the array.
        For each number, update its frequency using `get()`.

        Then sort the dictionary items based on their frequencies in descending
        order. Traverse the sorted elements and add the first `k` numbers to the
        result list. Once `k` elements have been collected, return the result.

        Time Complexity: O(n + m log m)

        Space Complexity: O(m)

        where `n` is the number of elements in `nums` and `m` is the number of
        distinct elements in `nums`.
"""

class Solution:
    def topKFrequent(self, nums, k):
       
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        l = []

        count = 0

        for num, freq in sorted(d.items(), key=lambda x: x[1], reverse=True):
            l.append(num)
            count += 1

            if count == k:
                break

        return l