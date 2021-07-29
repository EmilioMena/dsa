#LC 101

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Recursive

class RecursiveSolution(object):
    def isSymmetric(self, root):
        return evaluate(root.left, root.right)



def evaluate(left, right):
    if left is None and right is None:
        return True

    if (left and not right) or (right and not left):
        return False

    if left.val!= right.val:
        return False

    return evaluate(left.right, right.left) and evaluate(left.left, right.right)

# Iterative

from collections import deque # Queue

class IterativeSolution(object):
    def isSymmetric(self, root):
        stack = deque()
        stack.append(root.left)
        stack.append(root.right)
        while len(stack) > 0:
            left = stack.popleft()
            right = stack.popleft()

            if left and right:
                if left.val == right.val:
                    stack.append(left.left)
                    stack.append(right.right)
                    stack.append(left.right)
                    stack.append(right.left)
                else:
                    return False
            elif (left and not right) or (right and not left):
                    return False

        return True
