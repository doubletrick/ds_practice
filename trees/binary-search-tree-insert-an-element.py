"""
 * Sample input:
 *
 *           4
 *         /   \
 *        2     6
 *       / \   / \
 *      1   3 5   7


"""
class TreeNode:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def InsertItem(node,data):

    if node:
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                InsertItem(node.left,data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                InsertItem(node.right,data)
    else:
        node.data = data
        

if __name__ == '__main__':
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    InsertItem(root,0)
    InsertItem(root,10)
    