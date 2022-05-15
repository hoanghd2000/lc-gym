class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Dict of values
        one_char = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        two_char = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        sum = 0
        i = 0
        
        while i < len(s):
            if s[i:i+2] in two_char.keys():
                sum += two_char[s[i:i+2]]
                i += 2
            else:
                sum += one_char[s[i]]
                i += 1
        
        return sum