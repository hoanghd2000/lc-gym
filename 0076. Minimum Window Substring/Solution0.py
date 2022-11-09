class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if len(s) < len(t):
            return ""
        
        # find char_dict for t
        char_dict_t = {}
        for ch in t:
            if ch in char_dict_t:
                char_dict_t[ch] += 1
            else:
                char_dict_t[ch] = 1
        
        # Sliding window for s
        l = 0
        char_dict_s = {}
        res = (len(s)+1, 0, len(s))
        for r in range(len(s)):
            if s[r] in char_dict_s:
                char_dict_s[s[r]] += 1  
            else:
                char_dict_s[s[r]] = 1
        
            found = True
            for char in char_dict_t:
                if char not in char_dict_s or char_dict_s[char] < char_dict_t[char]:
                    found = False
                    break
            
            if found:
                while found and l < len(s):
                    res = min(res, (r-l+1, l, r))
                    if char_dict_s[s[l]] == 1:
                        char_dict_s.pop(s[l])
                    else:
                        char_dict_s[s[l]] -= 1
                    l += 1
                    for char in char_dict_t:
                        if char not in char_dict_s or char_dict_s[char] < char_dict_t[char]:
                            found = False
                            break
        
        return "" if res[0] == len(s)+1 else s[res[1]:res[2]+1]