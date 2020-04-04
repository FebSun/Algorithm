#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 10:02
# @Author  : FebSun
# @FileName: climbing_stairs.py
# @Software: PyCharm

# 题干：
#     假设你正在爬楼梯，需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 思路：
#     假设总共20层，现在张三站在了20层，那么他最后一步，是怎么到达20层的呢？
#     张三有两种选择：
#         1、从19层，走一步，到达20层
#         2、从18层，走两步，到达20层
#     即stair(20) = stair(19) + stair(18)


def climbing_stairs(n):
    stairs = 0
    if n == 1:
        stairs = 1
    elif n == 2:
        stairs = 2
    else:
        stairs = climbing_stairs(n-1) + climbing_stairs(n -2)
    return stairs


if __name__ == "__main__":
    print(climbing_stairs(10))
