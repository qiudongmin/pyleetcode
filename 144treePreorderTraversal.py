#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

from myleetcode import TreeNode


class Solution(object):

    def preorderTraversal(self, root):
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


if __name__ == "__main__":
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.right.left = TreeNode(3)

    s = Solution()
    print s.preorderTraversal(a)
