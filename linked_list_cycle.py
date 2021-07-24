# LC 141
# runtime beats 94%
# memory usage beats 99.94%

# not in place, modifies the linked list. See tortoise and hare algorithm for better solution 
class Solution(object):
    def hasCycle(self, head):

        prev = current = head

        while current and current.next != 'SENTINAL':
            current = current.next
            prev.next = 'SENTINAL'

            prev = current

        if current is None:
            return False
        else:
            return True

