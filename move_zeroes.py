"""
LC 283
runtime beats 97.56%
memory beats 72.47%
"""

class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+= 1
        
        for i in range(j, len(nums), 1):
            nums[i] = 0