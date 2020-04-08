"""
 * Sample input:
 *
 *           1
 *         /   \
 *        2     3
 *       / \   / \
 *      4   5 6   7
 *
 *
 * Expected output:
 *
 *  [1,2,4,5,3,6,7]
 *
 *
 * Algorithm:
 * 1. create a stack and add the root node
 * 2. loop while pop from stack and get data from node
 * 3. visit right node and then right node
 *
 
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PreOrderTraversal(root):

    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(PreOrderTraversal(root))
