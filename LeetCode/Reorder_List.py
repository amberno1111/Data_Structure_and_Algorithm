# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You must do this in-place without altering the nodes' values.
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路，先把链表分为两段，然后反转后半部分链表，最后遍历前半部分，并把后半部分链表一个个插入
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:

            return
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        current, prev.next = slow, None
        prev1 = None
        while current:
            current.next, prev1, current = prev1, current, current.next
        l1, l2 = head, prev1
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            current.next, current, l1 = l1, l1, l1.next
            current.next, current, l2 = l2, l2, l2.next
        head = dummy.next
        # 因为题目要求不返回，因此这里不用写return head，也正是因为此，上一行要把你最后要返回的那个链表赋值给head
        return
















