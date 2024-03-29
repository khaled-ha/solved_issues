# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Write your solution in below function
def sumOfLeftLeaves(root: TreeNode):
    """
    :type root: TreeNode - Node representing the root of the tree
    :rtype: int: sum of left leaves
    """
    result = []
    if root.left:
        return sumOfLeftLeaves(root.left)
    if not root.left:
        return root.val
    if root. right:
        return sumOfLeftLeaves(root.right)

    return result

# Don't change anything below this line
def createTree(arr):
    if arr is None or len(arr) == 0 or not arr[0].isnumeric():
        return None

    treeNodeQueue = []
    integerQueue = []

    for a in arr:
        integerQueue.append(a)

    treeNode = TreeNode(int(integerQueue.pop(0)))
    treeNodeQueue.append(treeNode)

    while integerQueue != []:
        leftVal = None if (integerQueue == []) else integerQueue.pop(0)
        rightVal = None if (integerQueue == []) else integerQueue.pop(0)
        current = treeNodeQueue.pop(0)

        if leftVal and leftVal.isnumeric():
            left = TreeNode(int(leftVal))
            current.left = left
            treeNodeQueue.append(left)

        if rightVal and rightVal.isnumeric():
            right = TreeNode(int(rightVal))
            current.right = right
            treeNodeQueue.append(right)

    return treeNode


if __name__ == "__main__":
    line = input()
    components = line.strip().split(",")
    root = createTree(components)
    print(sumOfLeftLeaves(root))