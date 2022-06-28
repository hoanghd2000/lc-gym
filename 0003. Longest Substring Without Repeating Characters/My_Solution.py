class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        char_set = {}
        l = r = 0
        lar_l = lar_r = 0
        
        while r < len(s):
            if s[r] in char_set:
                l = char_set[s[r]] + 1
                r = char_set[s[r]]
                char_set = {}
            else:
                char_set[s[r]] = r
                if r - l > lar_r - lar_l:
                    lar_l = l
                    lar_r = r
            r += 1
        
        return lar_r - lar_l + 1