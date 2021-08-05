"""
LC 198

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        max_at_house = [-1] * len(nums)
        max_three_before = -1

        for i in range(len(nums)):
            if i - 2 < 0:
                max_at_house[i] = nums[i]
            else:
                max_at_house[i] = max(max_at_house[i-2] + nums[i], nums[i])

            if i - 3 >= 0:
                max_three_before = max(max_at_house[i-3], max_three_before)
                max_at_house[i] = max(max_at_house[i], nums[i] + max_three_before)

        return max(max_at_house)

