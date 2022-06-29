from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        len_p = len(p)
        
        # Char freq counter for p and substring of s of length len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[-1] + s[:len_p-1])
        
#         # Function to check if 2 strings are anagrams of each other
#         def areAnagrams(s: str, p: str) -> bool:
#             if len(s) != len(p):
#                 return False
            
#             counter_s = Counter(s)
#             counter_p = Counter(p)
            
#             for char in counter_s:
#                 if counter_s[char] != counter_p[char]:
#                     return False
#             return True
        
        # Iterate through each substring in s of length len(p)
        for i in range(len(s)-len_p+1):
            # Update the char freq counter for the current substring of s
            counter_s[s[i-1]] -= 1
            counter_s[s[i+len_p-1]] += 1
            
            # check if p and substring of s are anagrams of each other
            are_anagrams = True
            for char in counter_s:
                if counter_s[char] != counter_p[char]:
                    are_anagrams = False
                    break
            if are_anagrams:
                ans.append(i)
        
        return ans