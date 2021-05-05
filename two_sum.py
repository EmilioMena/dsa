"""
LC 1
"""

class Solution(object):
    def twoSum(self, nums, target):
        complements = {}
        
        for i, n in enumerate(nums):
            if n in complements:
                return [i, complements[n]]
            else:
                complements[target - n] = i