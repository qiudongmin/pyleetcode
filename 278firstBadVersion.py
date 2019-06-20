#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    l = 1
    r = n
    while l < r:
        mid = l + (r - l) / 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1
    return l


def isBadVersion(i):
    if i >= 5:
        return True
    else:
        return False


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) / 2
        print l, mid, r
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    #if l == len(nums) - 1:
    #    return l + 1
    return l

if __name__ == "__main__":
    #print searchInsert([1,2,3,4],5)
    numRows = 5
    res = []
    if numRows == 1:
        print [[1]]
    elif numRows == 2:
        print [[1], [1, 1]]
    else:
        res.append([1])
        res.append([1, 1])
        for i in range(2, numRows):
            res.append([1] * (i + 1))
            for j in range(1, i/2 + 1):
                print res[i-1]
                print res[i]
                print i,j
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
                res[i][i - j] = res[i][j]
        print res
