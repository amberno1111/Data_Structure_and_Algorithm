# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
# Notes:
#
#     If the two linked lists have no intersection at all, return null.
#     The linked lists must retain their original structure after the function returns.
#     You may assume there are no cycles anywhere in the entire linked structure.
#     Your code should preferably run in O(n) time and use only O(1) memory.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路很简单，首先遍历两个链表，得出各自的长度，假设两个链表，A, B，各自的长度是 a, b，假设 a > b
# 然后把教程链表的指针移动到剩下的长度和较短链表一样的位置(也就是把A的指针从头指针移动到a-b的位置)
# 两个链表同时开始一个一个的移动并比较，遇到的第一个相等的节点就是交叉节点
# Explanation: Without loss of generation, let's assume list A is k elements longer than list B. (k>=0)
# If list A is as long as list B, then obviously the returned node will be the intersection if there is an intersection,
# or null if there is no intersection.
# If list A is longer than list b, then when b reaches the end of list, a is still k nodes away from the end.
# Then b goes to the head of list A, continue until a reaches the end of list and goes back to the head of list B.
# At this point, b is k nodes away from the head of list A. Since list A is k elements longer than list B,
# we can conclude that both a and b are both lengthOf(list B) away from the end of the list
# (regardless of the existence of the intersection).
# That means a and b are same-length away from the intersection (or null).
# From now on, continue the loop, until we find the intersection (or null).
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
