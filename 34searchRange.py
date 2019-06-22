#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums) - 1
        res = []
        while lo < hi:
            mid = (lo + hi) / 2
            print lo, mid, hi
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        res.append(lo)

        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            print lo, mid, hi
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        print lo,hi
        if nums[hi] != target:
            res.append(hi - 1)
        else:
            res.append(hi)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.searchRange([1], 1)
