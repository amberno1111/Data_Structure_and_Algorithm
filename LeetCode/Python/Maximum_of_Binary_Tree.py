# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# 递归解法，关于树的问题有很多都可以使用递归解法，当然也可以使用BFS


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class BFSSolution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        node_list, depth = [root], 0
        while node_list:
            bfs_nodelist = []
            while node_list:
                node = node_list.pop()
                if node.left:
                    bfs_nodelist.append(node.left)
                if node.right:
                    bfs_nodelist.append(node.right)
            depth += 1
            node_list = bfs_nodelist
        return depth
