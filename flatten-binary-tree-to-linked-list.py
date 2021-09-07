"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

   1        1
 2   5  =>    2
3 4   6         3
                  4
                    5
                      6

"""
class Solution(object):
    
    """
    O(n) time
    O(1) space
    
    1) Find the rightmost node of the left side of the tree
    2) Set the right child of this 'rightmost' node to be the right side of the tree
    3) Move the left side of the tree to the right
    4) Set the left side to be None
    
    The initution behind this is that since it's a preorder traversal, the right side of the tree will come after
    the rightmost node on the left side of the tree.
    
    Continue doing for the rest of the tree
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return None

        node = root
        while node:
            
            # 'rightmost node'
            left = node.left

            if left:
                
                # 1) find the rightmost node on the left side of the tree
                while left.right or left.left:
                    left = left.right if left.right else left.left
                    
                # 2) set the right child of our rightmost node to the right child of the current tree
                left.right = node.right
                
                # 3) move the left side to the right
                node.right = node.left
                
                # 4) set left side to none
                node.left = None
            
            # Continue doing this until the end of the inorder traversal
            node = node.right
            
    
"""
O(n) time
O(n) space

Iterative preorder traversal with stack (can be done recursively too). 
Add all items in another stack to keep track of them for later

Finally copy them into the array
"""
def flatten(self, root):
    stack = [root]
    nodes = []
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            nodes.append(node)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    for i in range(1, len(nodes)):
        root.left = None
        root.right = nodes[i]
        root = root.right

