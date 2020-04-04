#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 14:06
# @Author  : FebSun
# @FileName: merge_sort.py
# @Software: PyCharm

import random
# 归并排序，采用分而治之的原理：
#     拆分：
#         1、将一个序列从中间位置分成两个序列
#         2、在将这两个子序列按照第一步继续二分下去
#         3、到所有子序列的长度都为1，也就是不可以再二分截止
#     合并：
#         1、按照最后分开的两个数排序后绑定
#         2、再往上一层，将两组数列排序后绑定
#         3、直到变成一个数列


def merge(left, right):
    # 相当蠢的办法，还容易出错！！
    # extend()方法也是比较蠢得，直接“+”

    # l_pos, r_pos = 0, 0
    # result = []
    # while l_pos < len(left) and r_pos < len(right):
    #     if left[l_pos] < right[r_pos]:
    #         result.append(left[l_pos])
    #         l_pos += 1
    #     else:
    #         result.append(right[r_pos])
    #         r_pos += 1
    # if l_pos < len(left):
    #     result.extend(left[l_pos:])
    # if r_pos < len(right):
    #     result.extend(right[r_pos:])
    # return result
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(arr):
    length = len(arr)
    mid = length // 2
    if length == 1:
        return arr
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == "__main__":
    test_arr = list(range(500))
    random.shuffle(test_arr)
    sorted_arr = merge_sort(test_arr)
    print(sorted_arr)
