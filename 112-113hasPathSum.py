#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

from myleetcode import TreeNode


class Solution(object):

    def hasPathSum112(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum - root.val == 0
        return self.hasPathSum112(root.left, sum - root.val) or self.hasPathSum112(root.right, sum - root.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        alist = []
        res, alist = self.hasPathSum113(root, sum, res, alist)
        return res

    def hasPathSum113(self, root, sum, res, alist):
        """
        :type root: TreeNode
        :type sum: int
        :type res: List[List[int]]
        :type alist: List[int]
        :rtype: List[int], List[List[int]]
        """
        if not root:
            return res, alist
        alist.append(root.val)
        if not root.left and not root.right and sum - root.val == 0:
            tmp = []
            tmp += alist
            res.append(tmp)
        res, alist = self.hasPathSum113(root.left, sum - root.val, res, alist)
        res, alist = self.hasPathSum113(root.right, sum - root.val, res, alist)
        alist.pop()
        return res, alist


if __name__ == "__main__":

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

    s = Solution()
    print s.pathSum(rt, 22)
