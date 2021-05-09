"""
LC 125

runtime beats 44.07%
memory beats 76.46%

O(n) solution
"""

class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) -1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True