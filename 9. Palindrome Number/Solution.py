class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        l = len(x)
        
        for i in range(l/2):
            if x[i] != x[l-1-i]:
                return False
        
        return True