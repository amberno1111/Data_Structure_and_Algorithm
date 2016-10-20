# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 合并K个已排序的数组，并分析整个算法的复杂度。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路：将每个链表的表头元素取出来，使用堆排序，因为k个链表中都排好序了，因此每次取堆顶的元素就是k个链表中的最小值，可以将其合并到合并链表中，再将这个元素的指针指向的下一个元素也加入到堆中，再调整堆，取出堆顶，合并链表。。。。以此类推，直到堆为空时，链表合并完毕。
# 妈的智障，还不如吧全部的节点值都去取出来，然后来个堆排序，最后挨个建立节点，复杂度也是O(n log n)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for listnode in lists:
            while listnode:
                heap.append(listnode.val)
                listnode = listnode.next
        heap.sort()
        res = p = ListNode(0)
        for i in heap:
            p.next = p = ListNode(i)
        return res.next


# 还有一种思路是归并排序，先分成两个子任务，然后递归求子任务，最后回溯回来。这个题目也是这样，先把k个list分成两半，然后继续划分，知道剩下两个list就合并起来，合并时会用到 Merge Two Sorted Lists 这道题





