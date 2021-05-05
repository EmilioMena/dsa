"""
LC 350
"""

"""
1) extra space with using hashmap
runtime beats 94.04%
memory beats 69.14%
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = {}
        result = []
        for num in nums1:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        
        for num in nums2:
            if num in nums and nums[num] -1 >= 0:
                result.append(num)
                nums[num] -= 1
        return result

"""
2) binary search to optimize already sorted arrays
runtime beats 33.82%
memory beats 86.25%
"""

class Solution(object):
    def bsearch(self, array, left, right, z):
        middle = (right + left) // 2
        if left > right:
            return False
        elif array[middle] > z:
            return self.bsearch(array, left, middle-1, z)
        elif array[middle] < z:
            return self.bsearch(array, middle+1, right, z)
        else:
            return True
        
    def intersect(self, nums1, nums2):
        if len(nums1) >= len(nums2):
            search_array = nums1
            static_array = nums2
        else:
            search_array = nums2
            static_array = nums1
        
        result = []
        search_array.sort()
        for n in static_array:
            if self.bsearch(search_array, 0, len(search_array)-1, n):
                result.append(n)
                search_array.remove(n)
        return result