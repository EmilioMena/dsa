"""
LC 189
"""
class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        result = [0]* length
        for i in range(length):
            offset = (i + k)%n
            result[offset] = nums[i]
        
        for i in range(length):
            nums[i] = result[i]