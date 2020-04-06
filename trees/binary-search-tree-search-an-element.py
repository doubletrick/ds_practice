# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:33:17 2020

@author: Rajkumar
"""

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

def SearchItem(node,n):

    found = False
    
    while node and not found:
        if node.data == n:
            found = True
        elif n < node.data:
            node = node.left
        elif n > node.data:
            node = node.right
    
    return found

if __name__ == '__main__':
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    print(SearchItem(root,5))
    print(SearchItem(root,10))