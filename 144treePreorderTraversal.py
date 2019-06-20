#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    r = root
    stack = []
    ans = []
    while r or len(stack) > 0:
        if r:
            ans.append(r.val)
            stack.append(r)
            r = r.left
            continue
        r = stack.pop()
        r = r.right

    return ans

a = TreeNode(1)
a.right = TreeNode(2)
a.right.left = TreeNode(3)
print preorderTraversal(a)