#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if target == nums[mid]:
                return mid
            elif not (nums[l] <= nums[mid]) ^ (target < nums[mid]) ^ (target < nums[l]):
                r = mid
            else:
                l = mid + 1
        return l if (l == r and nums[l] == target) else -1


if __name__ == "__main__":
    s = Solution()
    print s.search([1,3], 3)