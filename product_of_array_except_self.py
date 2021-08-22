"""
"""
# O(n) time, O(n) space
# Create two arrays left and right.
# Left holds the product of all values before index i
# Right holds the product of all values after index i
# e.g
# nums = [1,2,3,4]
# left = [1,2,6,24]
# right = [24,24,12,4]
# Then result = left[i]*right[i]

class Solution(object):    
    def productExceptSelf(self, nums):
        l = len(nums)
        left = [None]*len(nums)
        right = [None]*len(nums)
        result = [None]*len(nums)
        
        left[0] = nums[0]
        right[l-1] = nums[l-1]
        for i in range(1, len(nums)):
            left[i] = nums[i]*left[i-1]
            right[l-1-i] = nums[l-1-i]*right[l-i]
            
        result[0] = right[1]
        result[-1] = left[-2]
        for i in range(1, len(nums)-1):
            result[i] = left[i-1]*right[i+1]
            
        return result

# make it O(1) space by making result left and then calculating right on the go

class Solution(object):    
    def productExceptSelf(self, nums):
        length = len(nums)
        result = [None]*len(nums)
        
        result[0] = 1
        for i in range(1, length):
            result[i] = result[i-1]*nums[i-1]
        
        right = 1
        for i in reversed(range(length)):
            result[i] = result[i]*right
            right = right*nums[i]
            
        return result
        
