# Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL
# 这里的k可能是比链表长度要大的数字，因此实际旋转的位置就是k%len(list)。如果这个计算结果等于零或者等于len(list)，列表是不用旋转的。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        n, cur = 1, head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head
        cur, tail = head, cur
        for i in range(n - k % n):
            tail = cur
            cur = cur.next
        tail.next = None
        return cur




