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
 *  [4,5,2,6,7,3,1]
 *
 *
 * Algorithm:
 * 1. create two stacks: stack and level
 * 2. loop while and add nodes to the level stack
 * 3. visit left node and then right node
 * 4. loop while and pop node from level and get data
 *

"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PostOrderTraversal(root):

    stack = [root]
    level = []
    result = []
    while stack:
        node = stack.pop()
        level.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while level:
        node = level.pop()
        result.append(node.data)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(PostOrderTraversal(root))
