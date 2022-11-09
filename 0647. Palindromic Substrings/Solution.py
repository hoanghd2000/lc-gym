class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        count = 0
        
        for i in range(len_s):
            l = r = i
            while l >= 0 and r < len_s and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len_s and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
        return count