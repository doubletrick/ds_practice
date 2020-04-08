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
 *  [4,2,5,1,6,3,7]
 *
 *
 * Algorithm:
 * 1. create a stack
 * 2. loop while stack or node
 * 3. visit left node and assign that to node
 * 4. after left node is exhausted, pop an item from stack
 *    and get the data
 * 5. visit right node and assign that to node

"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def InOrderTraversal(root):

    stack = []
    result = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(InOrderTraversal(root))
