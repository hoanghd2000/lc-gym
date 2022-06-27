class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = {chr(i+97):0 for i in range(26)}
        t_counter = {chr(i+97):0 for i in range(26)}

        
        # Character frequency counting for both s and t
        for i in range(len(s)):
            s_counter[s[i]] += 1
            t_counter[t[i]] += 1
        
        # Checking if s and t are anagrams
        for i in range(26):
            if s_counter[chr(i+97)] != t_counter[chr(i+97)]:
                return False
        return True