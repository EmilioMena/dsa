"""
LC 206
runtime beats 92.20%
memory beats 30.76%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        prev = None
        current = head
        
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
