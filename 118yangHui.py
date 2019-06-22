#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
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
                for j in range(1, i / 2 + 1):
                    print res[i - 1]
                    print res[i]
                    print i, j
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
                    res[i][i - j] = res[i][j]
            return res


if __name__ == "__main__":
    s = Solution()
    print s.generate(5)
