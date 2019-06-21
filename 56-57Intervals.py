#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%d, %d]' % (self.start, self.end)


def merge(intervals):
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


def insert(intervals, newInterval):
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
    print merge([Interval(0,1),Interval(2,3)])