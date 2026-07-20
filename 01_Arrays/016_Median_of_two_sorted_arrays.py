"""
Problem: Median of Two Sorted Arrays

Platform: LeetCode

Difficulty: Hard

Approach:

Apply Binary Search on the smaller of the two sorted arrays to find a valid
partition. The partition divides both arrays into left and right halves such
that every element in the left half is less than or equal to every element in
the right half. At each step, compute the partition indices for both arrays and
determine the boundary elements around the partitions. If the partition is
valid, compute the median based on whether the total number of elements is even
or odd. If the left partition of the first array contains an element greater
than the right partition of the second array, move the search to the left;
otherwise, move it to the right. Continue until the correct partition is found.

Time Complexity: O(log(min(n, m)))

Space Complexity: O(1)
"""
class Solution(object):
    def findMedianSortedArrays(self, a, b):
        n1 = len(a)
        n2 = len(b)

        if n1 > n2:
            return self.findMedianSortedArrays(b, a)

        begin = 0
        end = n1

        while begin <= end:
            i1 = (begin + end) // 2
            i2 = ((n1 + n2 + 1) // 2) - i1

            max1 = float('-inf') if i1 == 0 else a[i1 - 1]
            min1 = float('inf') if i1 == n1 else a[i1]
            max2 = float('-inf') if i2 == 0 else b[i2 - 1]
            min2 = float('inf') if i2 == n2 else b[i2]

            if max1 <= min2 and max2 <= min1:
                if (n1 + n2) % 2 == 0:
                    return (max(max1, max2) + min(min1, min2)) / 2.0
                else:
                    return max(max1, max2)

            if max1 > min2:
                end = i1 - 1
            else:
                begin = i1 + 1

        return -1