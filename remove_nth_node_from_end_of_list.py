"""
LC 19
runtime beats 91.96%
memory 69.91%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(val=0, next=head)
        
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
            
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
