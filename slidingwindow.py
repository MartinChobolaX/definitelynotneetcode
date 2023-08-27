""""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
""""

from collections import Counter
class Solution(object):
    def custom_counter(self,string):
        char_count = Counter(string)
        
        # Include keys with zero counts
        all_chars = set(string)
        for char in all_chars:
            if char in char_count:
                char_count[char] = 0
        
        return char_count
    def characterReplacement(self,s,k):
        l,r = 0,0
        char_freq = self.custom_counter(s)
        longest_sub = 1
        while r < len(s):
            char_freq[s[r]] += 1
            while (r - l + 1) - max(char_freq.values()) > k:
                char_freq[s[l]] -=1
                l += 1
            r += 1
            longest_sub = max(longest_sub,r-l)
        return longest_sub


    
