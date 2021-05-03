"""
LC 26
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        nex = 1
        while nex < len(nums):
            if nums[curr] != nums[nex]:
                curr += 1
                nums[curr] = nums[nex]
            nex += 1
        return curr + 1