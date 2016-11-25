# Invert a binary tree.
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归解法
class RecuSolution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# 暴力解法
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            nodes = [root]
            while nodes:
                node = nodes.pop()
                node.right, node.left = node.left, node.right
                if node.right:
                    nodes.append(node.right)
                if node.left:
                    nodes.append(node.left)
        return root
