# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路，找到链表的中心，然后翻转前半部分链表，再比较
# 寻找中心的方法，设置快慢两个指针，快指针走到底的时候，慢指针正好在中间
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            tail = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
