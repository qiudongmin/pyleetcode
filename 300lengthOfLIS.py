#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxL = 0
        """
        tail数组的定义：长度为i + 1的上升子序列的末尾最小是几
        """
        tail = [0 for i in range(len(nums))]
        for n in nums:
            lo, hi = 0, maxL
            while lo < hi:
                mid = lo + (hi - lo) / 2
                if tail[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            tail[lo] = n
            if lo == maxL:
                maxL += 1
        return maxL


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLIS([1,2,3])
