"""
LC 88

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        r_nums1 = m-1
        r_nums2 = n-1
        i = len(nums1) - 1
        while r_nums1 >= 0 and r_nums2 >=0:
            if nums1[r_nums1] > nums2[r_nums2]:
                nums1[i] = nums1[r_nums1]
                r_nums1 -= 1
            else:
                nums1[i] = nums2[r_nums2]
                r_nums2 -= 1

            i -= 1

        while r_nums2 >= 0:
            nums1[i] = nums2[r_nums2]
            i-= 1
            r_nums2-=1


