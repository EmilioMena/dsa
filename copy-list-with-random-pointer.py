"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy_copy = Node(0)
        copy = dummy_copy
        
        old_node = head 
        node_dict = {}
        while old_node is not None:            
            copy.next = Node(old_node.val)
            node_dict[old_node] = copy.next     
            
            copy = copy.next
            old_node = old_node.next
        
        old_node = head
        copy = dummy_copy.next
        while old_node is not None:
            if old_node.random:
                copy.random = node_dict[old_node.random]
            
            copy = copy.next
            old_node = old_node.next
        
        return dummy_copy.next
