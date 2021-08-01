"""
LC 108

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""

class Solution(object):
    def sortedArrayToBST(self, nums):
        left, right= 0, len(nums) -1
        return recurse(left, right, nums)


def recurse(left, right, nums):
    if right >= left:
        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = recurse(left, mid - 1, nums)
        node.right = recurse(mid + 1, right, nums)
    else:
        return None

    return node
