class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_freq_ran = [0] * 26
        char_freq_mag = [0] * 26
        
        for char in ransomNote:
            char_freq_ran[ord(char)-ord('a')] += 1
        for char in magazine:
            char_freq_mag[ord(char)-ord('a')] += 1
        for i in range(26):
            if char_freq_ran[i] > char_freq_mag[i]:
                return False
        return True