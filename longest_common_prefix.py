"""
LC 14

runtime beats 93.84%
memory beats 64.13%

vertical scaling option
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = len(strs[0])
        for word in strs:
            min_length = len(word) if len(word) < min_length else min_length
        
        result = ""
        for i in range(min_length):
            l = strs[0][i]
            for word in strs:
                if word[i] != l:
                    return result
            result += l
            
        return result
