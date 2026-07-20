"""
Problem: Plus One

Platform: LeetCode

Difficulty: Easy

Approach:

Treat the array as a decimal number where each element represents a digit.
Traverse the array from right to left and reconstruct the integer by multiplying
each digit with its corresponding place value. After forming the complete
number, increment it by one. Finally, convert the updated number back into a
list of digits and return the resulting array.

Time Complexity: O(n)

Space Complexity: O(n)
"""
class Solution(object):
    def plusOne(self, arr):
        num = 0
        pos = 1

        for i in range(len(arr) - 1, -1, -1):
            num += arr[i] * pos
            pos *= 10

        num += 1
        l = [int(d) for d in str(num)]

        return l