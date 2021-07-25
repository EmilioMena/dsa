# LC 98


# two ways to solve

# 1) since binary trees are sorted, do an in order traversal and check result

class Solution(object):
    def isValidBST(self, root):
        inOrderArray = inOrderTraverse(root, [])

        print(inOrderArray)
        for i in range(len(inOrderArray) - 1):
            if not (inOrderArray[i+1] > inOrderArray[i]):
                return False

        return True




def inOrderTraverse(node, result):
    if not node:
        return

    inOrderTraverse(node.left, result)
    result.append(node.val)
    inOrderTraverse(node.right, result)

    return result


# 2) pass down max and min allowed values to nodes and do a check at each level

class Solution(object):
    def isValidBST(self, root):
        return isValid(root, None, None)


def isValid(node, minVal, maxVal):
    if node is None:
        return True

    if (minVal is not None and node.val <= minVal) or (maxVal is not None and node.val >= maxVal):
        return False

    # for left children, max is parent value
    # for right childre, min is parent value
    return isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)

