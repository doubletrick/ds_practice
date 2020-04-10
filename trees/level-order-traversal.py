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
 *  [1,2,3,4,5,6,7]
 *
 *
 * Algorithm:
 * 1. create a stack
 * 2. loop while stack
 * 3. pop an item from stack and get the data
 * 4. visit left node and then right
 *

"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderTraversal(root):

    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(LevelOrderTraversal(root))
