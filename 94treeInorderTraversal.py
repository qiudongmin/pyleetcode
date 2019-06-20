#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    r = root
    stack = []
    ans = []
    while r or len(stack) > 0:
        if r:
            stack.append(r)
            r = r.left
            continue
        r = stack.pop()
        ans.append(r.val)
        r = r.right

    return ans


l1 = TreeNode(1)
l2 = TreeNode(2)
r2 = TreeNode(2)
l3 = TreeNode(3)
r3 = TreeNode(3)
l4 = TreeNode(4)
r4 = TreeNode(4)

l1.left = l2
l1.right = r2
l2.left = l3
r2.right = r3
l3.left = l4
r3.right = r4

