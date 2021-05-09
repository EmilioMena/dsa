"""
LC 344
runtime beats 58%
memory beats 55%

classic reverse string, two pointer approach
(condensed into one pointer bc python can index with -1)
"""

class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1 - i], s[i]