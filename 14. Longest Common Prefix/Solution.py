class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        for str in strs:
            if str == "":
                return ""
        
        prefix_length = 0
        done = False
        while not done:
            for i in range(1, len(strs)):
                if prefix_length > len(strs[0]) or prefix_length > len(strs[i]):
                    prefix_length -= 1
                    done = True
                    break
                if strs[0][:prefix_length+1] != strs[i][:prefix_length+1]:
                    done = True
                    break
            if not done:
                prefix_length += 1
        return strs[0][:prefix_length]