"""
Problem: Compare Version Numbers

Platform: LeetCode

Difficulty: Medium

Approach:

Split both version strings into their revision numbers and convert
each revision into an integer.

1. Split `version1` and `version2` using `.`.
2. Convert all revision strings into integers.
3. Compare corresponding revisions from both versions.
4. If a revision is smaller, return -1.
5. If a revision is larger, return 1.
6. If one version has remaining revisions, compare them with 0.
7. If all revisions are equal, return 0.

Key Idea:

Split the versions → convert revisions to integers → compare each
revision from left to right.

Time Complexity: O(n + m)

Space Complexity: O(n + m)

The split lists store the revisions of both version strings.
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l = version1.split('.')
        r = version2.split('.')

        for i in range(len(l)):
            l[i] = int(l[i])
        
        for i in range(len(r)):
            r[i] = int(r[i])
        
        i = 0
        j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                return -1
            elif l[i] > r[j]:
                return 1
            else:
                i += 1
                j += 1
        
        while i < len(l):
            if l[i] < 0:
                return -1
            elif l[i] > 0:
                return 1
            else:
                i += 1
        
        while j < len(r):
            if r[j] < 0:
                return 1
            elif r[j] > 0:
                return -1
            else:
                j += 1

        return 0