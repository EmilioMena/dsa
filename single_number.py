"""
LC 136: linear wihtout extra memory
runtime beats 73.45%
memory beats 83.02%
"""
class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        for i in range(0, len(nums), 2):
            if i+1 >= len(nums):
                return nums[i]
            elif nums[i] != nums[i+1]:
                return nums[i]