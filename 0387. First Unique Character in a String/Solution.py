class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Edge Case
        if len(s) == 1:
            return 0
        
        char_list = set()
        re_char_list = set()
        
        # Iterate through s
        for ch in s:
            if ch in char_list:
                re_char_list.add(ch)
            char_list.add(ch)
        
        # Iterate through s again, return the index of the first char c not in re_char_list. If cant find, return -1
        for i, ch in enumerate(s):
            if ch not in re_char_list:
                return i
        return -1