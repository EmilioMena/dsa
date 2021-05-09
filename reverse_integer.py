"""
LC 7
runtime beats 65.07%
memory beats 88.54%
"""

class Solution(object):
    def reverse(self, x):
        absolute = abs(x)
        size = len(str(absolute))
        result = 0
        for i in range(size -1, -1, -1):
            result += (absolute % 10) * 10**i
            absolute = absolute / 10
        
        if result < -2**31 or result > 2**31 -1:
            return 0
        return result if x >= 0 else result*-1