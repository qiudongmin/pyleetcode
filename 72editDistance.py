#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def minEditDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        # word1 变成 空 所需要的删除的步骤
        for i in range(1, l1 + 1):
            dp[i][0] = i

        # 空 变成 word2 所需要的添加的步骤
        for j in range(1, l2 + 1):
            dp[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i][j] = Min(delete,add,change) + 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[l1][l2]


if __name__ == "__main__":
    s = Solution()
    print s.minEditDistance("intention", "execution")
