#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

from myleetcode import ListNode
from myleetcode import ListNodeOP


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 创建头节点，之后用头节点引用整个链表
        # 因为头节点不会被改变，而数据节点head会被调整
        dummyhead = ListNode(-1)
        dummyhead.next = head
        pre = dummyhead.next
        cur = pre.next
        while cur:
            q = dummyhead
            p = q.next
            while p != cur and cur.val > p.val:
                q = p
                p = p.next

            # 调整节点
            if p != cur:
                pre.next = cur.next
                cur.next = p
                q.next = cur
                cur = pre.next
            else:
                cur = cur.next
                pre = pre.next

        return dummyhead.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        return self.mergeSort(head)

    def mergeSort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        q, p = head, head
        while p.next and p.next.next:
            p = p.next.next
            q = q.next
        r = q.next
        q.next = None
        l = head
        l = self.mergeSort(l)
        r = self.mergeSort(r)
        return self.merge(l, r)

    def merge(self, l, r):
        """
        :type l: ListNode
        :type r: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        cur = dummyhead
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if l:
            cur.next = l
        elif r:
            cur.next = r
        return dummyhead.next


if __name__ == "__main__":
    s = Solution()
    lnop = ListNodeOP()
    head = lnop.createList([-1,5,3,4,0])
    lnop.printList(s.sortList(head))
