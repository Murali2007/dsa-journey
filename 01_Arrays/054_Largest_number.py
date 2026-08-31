from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        """
        Problem: Largest Number

        Platform: LeetCode

        Difficulty: Medium

        Approach:

        Convert all numbers into strings so that they can be compared based on
        how they contribute to the final concatenated number. For every pair of
        numbers `a` and `b`, compare `a + b` with `b + a`. If `a + b` is larger,
        `a` should come before `b`; otherwise, `b` should come before `a`.
        Use `cmp_to_key()` to apply this custom comparison during sorting.

        After sorting, concatenate all the strings to form the largest possible
        number. If the first element is `"0"`, all elements must be zero, so
        return `"0"` instead of a string containing multiple zeros.

        Time Complexity: O(n log n × k)

        Space Complexity: O(n)

        where `n` is the number of elements and `k` is the maximum number of
        digits in an element.
        """
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1

        nums.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"

        return ''.join(nums)