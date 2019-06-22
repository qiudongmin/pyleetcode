#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

from myleetcode import TreeNode


class Solution(object):

    def postorderTraversal(self, root):
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


if __name__ == "__main__":
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.right.left = TreeNode(3)

    s = Solution()
    print s.postorderTraversal(a)
