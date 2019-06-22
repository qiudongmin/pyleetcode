#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n-1][m-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    dp[i][j] = 0 if dp[i][j - 1] == 0 else 1
                elif j == 0 and i > 0:
                    dp[i][j] = 0 if dp[i - 1][j] == 0 else 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n-1][m-1]

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        深度优先搜索
        """
        return 0


if __name__ == "__main__":
    s = Solution()
    print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
