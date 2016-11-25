# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 双指针, 一个跑一步,另一个跑两步,如果是一个环,除了在开始节点外,总是会在某个瞬间跑到同一个点上
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first, runner = head, head
        while first and first.next and runner and runner.next:
            first, runner = first.next, runner.next.next
            if first == runner:
                return True
        return False
