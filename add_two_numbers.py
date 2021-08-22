"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        dummy = result
        
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            if add >= 10:
                carry = 1
                result.next = ListNode(val=add % 10)
            else:
                result.next = ListNode(val=add)
                carry = 0
            
            result = result.next
            
            l1 = l1.next
            l2 = l2.next
            
        rest = l1 or l2
        
        if rest:
            while rest:
                add = carry + rest.val
                if add < 10:
                    result.next = ListNode(val=add)
                    carry = 0
                else:
                    result.next = ListNode(val=add%10)
                
                result = result.next
                rest = rest.next
            
        if carry == 1:
            result.next = ListNode(val=carry)
        

        return dummy.next
