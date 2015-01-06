# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None: # node is None
            return 0
        elif root.left is None and root.right is None: # has no children
            return 1
        elif root.left is None and root.right is not None: # has right child
            return 1 + self.minDepth(root.right)
        elif root.left is not None and root.right is None: # has left child
            return 1 + self.minDepth(root.left)
        else: # has both children
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
