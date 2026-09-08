"""
Problem: Group Anagrams

Platform: LeetCode

Difficulty: Medium

Approach:

Use a dictionary to group strings that are anagrams of each other.

1. Create an empty dictionary `d`.
2. Traverse every string in `strs`.
3. Sort the characters of the current string and join them to create
   a common key.
4. Anagrams contain the same characters with the same frequencies, so
   their sorted characters will be identical.
5. Use the sorted string as the dictionary key and append the original
   string to its corresponding list.
6. Finally, collect all dictionary values and return them.

Key Idea:

Create a canonical key for every word by sorting its characters.

Example:

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Keys:
    eat → aet
    tea → aet
    tan → ant
    ate → aet
    nat → ant
    bat → abt

Therefore:

    aet → ["eat", "tea", "ate"]
    ant → ["tan", "nat"]
    abt → ["bat"]

Time Complexity: O(n × k log k)

Where:
    n = number of strings
    k = maximum length of a string

Each string is sorted in O(k log k).

Space Complexity: O(n × k)

The dictionary stores all strings grouped by their sorted keys.

"""

class Solution:
    def groupAnagrams(self, strs) :
        d = {}

        for string in strs:
            key = ''.join(sorted(string))

            if key in d.keys():
                d[key].append(string)
            else:
                d[key] = [string]

        output = []

        for val in d.values():
            output.append(val)

        return output