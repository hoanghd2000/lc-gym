from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # list of 26 prime numbers, each mapped to a English lowercase char
        prime_no = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        
        res = {}
        
        # Processing and grouping for each str in strs
        for str in strs:
            prod = 1
            for char in str:
                prod *= prime_no[ord(char)-ord('a')]
            if prod not in res:
                res[prod] = [str]
            else:
                res[prod].append(str)
        
        return res.values()