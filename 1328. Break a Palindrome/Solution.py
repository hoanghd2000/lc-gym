class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        len_s = len(palindrome)
        
        # Edge Cases
        if len_s == 1:
            return ""
        
        for i in range(len_s//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:len_s-1] + 'b'