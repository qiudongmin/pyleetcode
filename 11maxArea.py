#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        l = 0
        r = len(height) - 1
        maxarea = 0
        while l < r:
            if height[l] > height[r]:
                maxarea = max(maxarea, (r - l) * height[r])
                r -= 1
            else:
                maxarea = max(maxarea, (r - l) * height[l])
                l += 1
        return maxarea


if __name__ == "__main__":
    s = Solution()
    print s.maxArea([1,8,6,2,5,4,8,3,7])
