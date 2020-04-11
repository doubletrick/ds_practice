"""
 * Sample input:
 *
 *          1
 *         / \
 *        3   5
 *       /   / \
 *      2   4   7
 *     / \   \
 *    9   6   8
 
 *
 * Expected output:
 *    1
 *    3 5
 *    2 4 7
 *    9 6 8

"""


class TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderPrint(root):

    stack = [root]
    while stack:
        level, result = list(), list()
        for node in stack:
            result.append(str(node.data))
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        stack = level
        print(' '.join(result))


if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(9)
    root.left.left.right = TreeNode(6)
    root.right.left.right = TreeNode(8)
    
    LevelOrderPrint(root)