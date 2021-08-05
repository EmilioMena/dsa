"""
LC 53

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        max_current = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            max_current = max(max_current + num, num)
            max_sum = max(max_sum, max_current)

        return max_sum
