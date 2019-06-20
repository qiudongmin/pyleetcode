#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _1hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    if not root.left and not root.right:
        return sum - root.val == 0
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

res = []
alist = []
def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return res
    alist.append(root.val)
    if not root.left and not root.right and sum-root.val == 0:
        a = []
        a += alist
        res.append(a)
    pathSum(root.left, sum-root.val)
    pathSum(root.right, sum-root.val)
    alist.pop()
    return res

rt = TreeNode(5)
l = TreeNode(4)
r = TreeNode(8)
ll = TreeNode(11)
rl = TreeNode(13)
rr = TreeNode(4)
lll = TreeNode(7)
llr = TreeNode(2)
rrl = TreeNode(5)
rrr = TreeNode(1)
rt.left = l
rt.right = r
l.left = ll
r.left = rl
r.right = rr
ll.left = lll
ll.right = llr
rr.left = rrl
rr.right = rrr
pathSum(rt, 22)


