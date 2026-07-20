"""
Problem: Longest Common Prefix

Platform: LeetCode

Difficulty: Easy

Approach:

Use the first string as the reference prefix. Traverse each character of this
string one by one and compare it with the character at the same position in
every other string. If any string ends before the current position or contains
a different character, return the prefix formed up to the previous position.
If all characters of the first string match across every string, then the first
string itself is the longest common prefix.

Time Complexity: O(n × m)

Space Complexity: O(1)
where n is the number of strings and m is the length of the shortest matching prefix.
"""
class Solution(object):
    def longestCommonPrefix(self, arr):
        string = arr[0]

        for i in range(len(string)):
            for j in range(1, len(arr)):
                if i == len(arr[j]):
                    return string[:i]

                if arr[j][i] != string[i]:
                    return string[:i]

        return string