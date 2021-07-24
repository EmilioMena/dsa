# LC 234
# runtime beats 85%
# memory usage beats 90%

# O(n) time and O(1) space solution 
class Solution(object):
    def isPalindrome(self, head):
        
        slow = fast = head
        
        # find mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        
        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # compare first half and reversed second half
        start = head
        end = prev
        
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        
        return True
                    
