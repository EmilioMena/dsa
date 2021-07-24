# LC 104
# Runtime beats 84%
# Memory storage beats 17%

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)      
        
        return max(maxLeft, maxRight) + 1
