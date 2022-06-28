class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        
        # Sliding window delimiters
        l = r = 0
        
        # Counting characters in sliding window
        count = {}
        for i in range(26):
            count[chr(i + ord('A'))] = 0
        
        while r < len(s):
            count[s[r]] += 1
            max_freq = max(count.values())
            
            # Expand the sliding window
            if r - l + 1 - max_freq <= k:
                ans = max(ans, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
            
            r += 1
        
        return ans