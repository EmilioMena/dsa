"""
LC 237
runtime beats 90.50%
memory beats 95.85%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        cutoff = node
        while cutoff.next is not None:
            cutoff = cutoff.next
            node.val = cutoff.val
            if cutoff.next is None:
                node.next = None
            else:
                node = node.next
                
