#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def zigConvert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        slen = len(s)
        n = 2 * numRows - 2
        if slen <= 1 or n == 0:
            return s
        k = slen / n
        m = slen % n
        ss = ''
        flag = True
        for y in range(numRows):
            if y == 0:
                t = k + 1 if m > 0 else k
                ss += ''.join([s[x * n + y] for x in range(t)])
            elif y == numRows - 1:
                t = k + 1 if m >= numRows else k
                ss += ''.join([s[x * n + y] for x in range(t)])
            else:
                for x in range(k):
                    ss += (s[x * n + y] + s[x * n + n - y])
                if y > m - 1:
                    continue
                elif m > numRows and n - m < y < numRows - 1:
                    ss += (s[k * n + y] + s[k * n + n - y])
                else:
                    ss += s[k * n + y]
        return ss


if __name__ == "__main__":
    s = Solution()
    print s.zigConvert('ABCDE', 4)
