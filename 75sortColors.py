#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 平移法 击败100%python
        # 每次移动0～p-1的串，和橡皮擦一样，先移的被后移的覆盖
        i, j, k = -1, -1, -1
        for p in range(len(nums)):
            if nums[p] == 0:
                k += 1
                j += 1
                i += 1
                nums[k] = 2
                nums[j] = 1
                nums[i] = 0
            elif nums[p] == 1:
                k += 1
                j += 1
                nums[k] = 2
                nums[j] = 1
            else:
                k += 1
                nums[k] = 2


if __name__ == "__main__":
    s = Solution()
    s.sortColors([2,0,2,1,1,0])
