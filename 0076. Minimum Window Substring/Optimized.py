from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if len(s) < len(t):
            return ""
        
        # find char_dict for t
        char_dict_t = Counter(t)
        required = len(char_dict_t)
        
        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in char_dict_t:
                filtered_s.append((i, char))
        
        # Sliding window for s
        l = 0
        formed = 0
        char_dict_s = {}
        res = (len(s)+1, 0, len(s))
        
        for r in range(len(filtered_s)):
            character = filtered_s[r][1]
            if character in char_dict_s:
                char_dict_s[character] += 1  
            else:
                char_dict_s[character] = 1
            
            if char_dict_s[character] == char_dict_t[character]:
                formed += 1
            
            while l <= r and formed == required:
                character = filtered_s[l][1]
                
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                res = min(res, (end - start + 1, start, end))
                    
                char_dict_s[character] -= 1
                if char_dict_s[character] < char_dict_t[character]:
                    formed -= 1
                l += 1
        
        return "" if res[0] == len(s)+1 else s[res[1]:res[2]+1]