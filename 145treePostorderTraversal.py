#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    r = root
    stack = []
    ans = []
    stack.append(r)
    while len(stack) > 0:
        r = stack.pop()
        ans.append(r.val)
        if r.left:
            stack.append(r.left)
        if r.right:
            stack.append(r.right)

    ans.reverse()
    return ans

a = TreeNode(1)
a.right = TreeNode(2)
a.right.left = TreeNode(3)
print postorderTraversal(a)
