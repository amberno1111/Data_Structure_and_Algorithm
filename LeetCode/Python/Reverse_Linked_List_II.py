# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # if head is None or head.next is None or m == n:
        #     return head
        # dummy = ListNode(0)
        # dummy.next = head
        # prev= dummy
        # for i in range(m - 1):
        #     prev, head= prev.next, head.next
        # prev.next = None
        # current, tail = head, head.next
        # for i in range(n - m):
        #     head, tail = head.next, tail.next
        # head.next = None
        # while current and current.next:
        #     tail, current, current.next = current, current.next, tail
        # prev.next = current
        # return dummy.next
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for i in range(m - 1):
            p = p.next
        curr = p.next
        for i in range(n - m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = p.next
            p.next = tmp
        return dummy.next

