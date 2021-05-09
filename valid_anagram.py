"""
LC 242

runtime beats 44.90%
memory beats 60.07%
O(n) solution
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1

        for letter in t:
            if letter in count:
                count[letter] -= 1
            else:
                return False
        
        for letter in count:
            if count[letter] != 0:
                return False
        
        return True