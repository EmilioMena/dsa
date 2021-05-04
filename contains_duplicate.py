"""
LC 217
runtime beats 55%
space beats 47%
"""

class Solution(object):
    def containsDuplicate(self, nums):
        unique = set()
        for n in nums:
            if n in unique:
                return True
            unique.add(n)
        return False