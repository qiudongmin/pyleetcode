#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


def maxProfit121(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    n = len(prices)
    dp = [0 for i in range(n)]
    minp = prices[0]
    for i in range(1, n):
        minp = min(minp, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - minp)
    return dp[n-1]


def maxProfit122(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxp = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxp += (prices[i] - prices[i-1])
    return maxp


def maxProfit123(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    days = len(prices) + 1
    dp = [[[0 for k in range(3)] for j in range(2)] for i in range(days)]
    for i in range(days):
        for j in range(2):
            for k in range(3):
                if k == 2 and j == 0:
                    continue
                if j > 0:
                    dp[i][j][k] = max(dp[])

