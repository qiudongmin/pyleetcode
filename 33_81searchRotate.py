#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def search33(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
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

    def search81(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if target == nums[mid]:
                return True
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
            elif not (nums[l] <= nums[mid]) ^ (target < nums[mid]) ^ (target < nums[l]):
                r = mid
            else:
                l = mid + 1
        return True if (l == r and nums[l] == target) else False


if __name__ == "__main__":
    s = Solution()
    print s.search81([2,5,6,0,0,1,2], 0)
