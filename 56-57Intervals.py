#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'

from myleetcode import Interval


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        lenlist = len(intervals)
        if lenlist < 2:
            return intervals
        intervals = sorted(intervals, key=lambda st: st.start)
        re = []
        for i in range(1, lenlist):
            pre = intervals[i - 1]
            now = intervals[i]
            if pre.end >= now.start:
                now.start = pre.start
                now.end = max(now.end, pre.end)
            else:
                re.append(pre)
        re.append(intervals[i])
        return re

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda st: st.start)
        lenlist = len(intervals)
        re = []
        for i in range(1, lenlist):
            pre = intervals[i - 1]
            now = intervals[i]
            if pre.end >= now.start:
                now.start = pre.start
                now.end = max(now.end, pre.end)
            else:
                re.append(pre)
        re.append(intervals[i])
        return re


if __name__ == "__main__":
    s = Solution()
    print s.merge([Interval(0,1),Interval(2,3)])
