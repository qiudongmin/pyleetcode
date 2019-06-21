#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return res
        nums = sorted(nums)
        length = len(nums)
        i = 0
        if nums[0] <= 0 <= nums[-1]:
            while i < length - 2:
                v = nums[i]
                if v > 0:
                    break
                l = i + 1
                r = length - 1
                while l < r:
                    lv = nums[l]
                    rv = nums[r]
                    if l >= r or v * rv > 0:
                        break
                    result = v + lv + rv
                    if result == 0:
                        res.append([v, lv, rv])
                    if result <= 0:
                        l += 1
                        while l < r and lv == nums[l]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and rv == nums[r]:
                            r -= 1
                i += 1
                while i < length - 2 and v == nums[i]:
                    i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
