#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%d, %d]' % (self.start, self.end)


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list operation
class ListNodeOP(object):

    def createList(self, nums):
        head = ListNode(0)
        p = head
        for n in nums:
            node = ListNode(n)
            p.next = node
            p = p.next
        return head.next

    def printList(self, head):
        s = ''
        while head:
            s += (str(head.val) + '->')
            head = head.next
        print s


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None