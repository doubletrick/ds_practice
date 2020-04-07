"""
Binary Search Tree

1. Left node is lesser than root node
2. Right node is greater than root node

"""

class BinarySearchTree:
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
