"""
LC 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        def climb(n, nums):
            if n == 1:
                return 1
            if n==2:
                return 2
            
            if nums[n]:
                return nums[n]
            
            nums[n] = climb(n-1, nums) + climb(n-2, nums)

            return nums[n]
        
        nums = [None] * (n+1)
        return climb(n, nums)
