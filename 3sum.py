"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# use 2sum solution as a helper. Sort the array to remove duplicates
# optimal complexity O(n^2)

class Solution(object):
    def threeSum(self, nums):
        nums.sort() # O(nlogn)
        triplets = []
        for i, n in enumerate(nums): # O(n)
            if i > 0 and n == nums[i-1]:
                continue
            triplet = self.twoSum(nums[i+1:], 0 - n, n) #O(n)
            if len(triplet) > 0:
                triplets.extend(triplet) # O(3n)

        return triplets


    def twoSum(self, nums, target, z):
        num_hash = {}
        for n in nums: #O(n)
            num_hash[n] = num_hash[n] + 1 if n in num_hash else 1

        result = []
        for i, n in enumerate(nums): #O(n)
            num_hash[n] -= 1

            if i > 0 and nums[i-1] == n:
                continue

            complement = target - n
            if complement in num_hash and num_hash[complement] > 0:
                result.append([z, n, complement])

        return result

