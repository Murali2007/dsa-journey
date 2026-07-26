"""
Problem: 3Sum Closest

Platform: LeetCode

Difficulty: Medium

Approach:

First, sort the array to enable the two-pointer technique. Initialize the
closest sum using the first three elements. Iterate through the array, treating
each element as the first number of a triplet. For every selected element, use
two pointers—one starting from the next index and the other from the end of the
array. Compute the current triplet sum and update the closest sum whenever it is
closer to the target than the previous best. If the current sum is smaller than
the target, move the left pointer to increase the sum. If it is larger, move the
right pointer to decrease the sum. If the current sum exactly equals the target,
return it immediately since no closer sum is possible. After examining all
possible triplets, return the closest sum found.

Time Complexity: O(n²)

Space Complexity: O(1)
"""
class Solution(object):
    def threeSumClosest(self, arr, target):
        arr.sort()
        n = len(arr)

        closest = arr[0] + arr[1] + arr[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return closest