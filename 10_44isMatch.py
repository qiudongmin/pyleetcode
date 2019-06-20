#!/usr/bin/python
# coding: utf-8
__author__ = 'qiudongmin'


def isMatch10(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    lenp = len(p) + 1
    lens = len(s) + 1
    # dp = [[False] * lenp] * lens
    # 不能用上面这种初始化方式，＊导致元素均为同一地址，后面改变单元格值时会一起变
    dp = [[False for j in range(lenp)] for i in range(lens)]
    dp[0][0] = True
    for i in range(lens):
        for j in range(1, lenp):
            if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                if i == 0 or (s[i - 1] != p[j - 2] and p[j - 2] != '.'):
                    dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i-1][j]
                #   dp[i][j-2] s中没有＊前面的字符
                #   dp[i][j-1] s[i] == p[j-1]
                #   dp[i-1][j] s[i] == s[i-1]

    return dp[lens - 1][lenp - 1]


def isMatch44(s, p):
    lenp = len(p) + 1
    lens = len(s) + 1
    dp = [[False for j in range(lenp)] for i in range(lens)]
    dp[0][0] = True
    for i in range(lens):
        for j in range(1, lenp):
            if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '?'):
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
                #   dp[i][j-1] *匹配空字符串
                #   dp[i-1][j] *匹配任意字符

    return dp[lens - 1][lenp - 1]

print isMatch44('acdcb', 'a*c?b')
