class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = s[0]
        max_len = 1
        len_s = len(s)
        
        for i in range(len_s):
            left = right = i
            while left >= 0 and right < len_s and s[left] == s[right]:
                if right - left + 1 > max_len:
                    result = s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1
            
            left = i
            right = i + 1
            while left >= 0 and right < len_s and s[left] == s[right]:
                if right-left + 1 > max_len:
                    result = s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1
        
        return result