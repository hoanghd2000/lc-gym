class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        
        # char_set stores the current index of a character in the string
        char_set = {}
        
        i = 0
        for j in range(len(s)):
            if s[j] in char_set:
                i = max(char_set[s[j]] + 1, i)
            ans = max(ans, j-i+1)
            char_set[s[j]] = j
        
        return ans