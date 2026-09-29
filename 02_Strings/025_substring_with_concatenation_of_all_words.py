"""
Problem: Substring with Concatenation of All Words

Platform: LeetCode

Difficulty: Hard

Approach:

Use a sliding window with fixed-size word chunks.

1. Calculate the length of each word and the total required window size.
2. Store the required frequency of each word in `need`.
3. Process the string using different starting offsets from 0 to `word_len - 1`.
4. Move the `right` pointer one complete word at a time.
5. If the current word is not required, clear the current window and restart
   from the next position.
6. If the word is required, add it to `have` and increase the word count.
7. If a word appears more times than required, move `left` forward by one word
   at a time until the window becomes valid.
8. When the window contains exactly `word_count` words, add its starting
   position to the result.

Key Idea:

Divide the string into word-sized chunks and maintain a sliding window
whose words must match the required frequencies.

Time Complexity: O(n)

Space Complexity: O(m)

where `n` is the length of `s` and `m` is the number of distinct words.
"""

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words) :
        word_len = len(words[0])
        word_count = len(words)
        n = word_len * word_count

        need = Counter(words)
        res = []

        for offset in range(word_len):
            right = offset
            left = offset

            have = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in need:
                    have.clear()
                    left = right
                    count = 0
                    continue
                
                have[word] += 1
                count += 1

                while have[word] > need[word]:
                    left_word = s[left:left+word_len]
                    have[left_word] -= 1
                    left += word_len
                    count -= 1
                
                if count == word_count:
                    res.append(left)

        return res
            
                
            
        

            



        