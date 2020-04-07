"""
 * Sample input:  
 * [1,2,3,4,5,6,7]
 *
 * Sample :
 *
 *          4
 *         / \
 *        2   6
 *       / \  / \
 *      1   3 5  7

"""

class Tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def List2BST(l,start,end):
    
    if start == end:
        node = Tree(l[start])
    else:
        m = (start + end) // 2
        node = Tree(l[m])
        node.left = List2BST(l,start, m-1)
        node.right = List2BST(l, m+1, end)
    return node
        
def LevelOrderTraversal(root):
    
    if root is None:
        return
    stack = [root]
    result = []
    while stack:
        node = stack.pop(0)
        result.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

        
if __name__ == '__main__':
    
    l = [1,2,3,4,5,6,7]
    
    root = List2BST(l,0,len(l)-1)
    
    print(LevelOrderTraversal(root))
    