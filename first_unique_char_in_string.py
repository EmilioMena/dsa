"""
LC 387
runtime beats 48.19%
memory too big :/

can be optimized to use less memory
"""

class Solution(object):
    def firstUniqChar(self, s):        
        directory = {}
        for i, letter in enumerate(s):
            if letter not in directory:
                directory[letter] = [i]
            else:
                directory[letter].append(i)
                
        non_rep = len(s)
        for letters, indicies in directory.items():
            if len(indicies) == 1:
                non_rep = indicies[0] if indicies[0] < non_rep else non_rep
        
        return non_rep if non_rep < len(s) else -1