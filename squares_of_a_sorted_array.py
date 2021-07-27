# LC 977

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution(object):
    def sortedSquares(self, nums):
        
        i, j = 0, len(nums) - 1
        
        k = len(nums) - 1
        
        result = [None] * len(nums)
        
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i]**2
                i+=1
            else:
                result[k] = nums[j]**2
                j-=1
                
            k -= 1
                
                
        return result
