"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.val == sum and root.left is None and root.right is None: # in leaf node satisfy the condition
            return True
        else:
            if self.hasPathSum(root.left, sum - root.val): # check to see left child is satisfy
                return True
            else:
                return self.hasPathSum(root.right, sum - root.val) # otherwise check to see left child is satisfy
