# Given a binary tree, return all root-to-leaf paths.
# For example, given the following binary tree:
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.right and not root.left:
            return [str(root.val)]
        left_path = self.binaryTreePaths(root.left)
        right_path = self.binaryTreePaths(root.right)
        all_path = left_path + right_path
        return ['%s->%s' % (root.val, path) for path in all_path]
