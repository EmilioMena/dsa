# LC 102

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        q = deque()
        q.appendleft(root)
        result = []

        while len(q) > 0:
            curr_level = []
            level_result = []
            # get all nodes in current level
            while len(q) > 0:
                curr_level.append(q.pop())

            for node in curr_level:
                if node:
                    level_result.append(node.val)
                    q.appendleft(node.left)
                    q.appendleft(node.right)

            if level_result:
                result.append(level_result)

        return result
