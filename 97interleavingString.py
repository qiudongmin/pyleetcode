#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l3 != l1 + l2:
            return False
        dp = [[False for j in range(l2 + 1)] for i in range(l1 + 1)]
        dp[0][0] = True
        # 定义好状态后，初始状态要考虑全面
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])

        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                """
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
                if s1[i-1] == s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                """
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[l1][l2]


if __name__ == "__main__":
    s = Solution()
    print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
