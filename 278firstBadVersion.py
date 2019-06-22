#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = l + (r - l) / 2
            if self.isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

    def isBadVersion(self, i):
        if i >= 5:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print s.firstBadVersion(5)
