"""
LC 286

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        if 0 not in nums:
            return 0

        max_n = max(nums)
        max_sum = (max_n * (max_n + 1)) / 2

        for num in nums:
            max_sum -= num

        if max_sum == 0:
            return max_n + 1
        return max_sum
