#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 10:34
# @Author  : FebSun
# @FileName: shell_sort.py
# @Software: PyCharm

import random
import datetime

# 希尔排序：
#     基于插入排序的时间复杂度较高，而且插入排序在处理基本有序的序列时表现更加优越，因此引入希尔排序。
#     希尔排序先将序列分组，分成{(length // 3) + 1}组，这个算法效率最高，每一组进行插入排序。
#     缩减分组，继续进行插入排序，知道变为一组，即最后的基本有序的序列进行插入排序


def shell_sort(arr):
    length = len(arr)
    gap = length
    while gap > 1:
        gap = (gap // 3) + 1
        print(gap)
        for i in range(gap):
            for j in range(i, length, gap):
                curose = arr[j]
                pos = j
                while pos > i and arr[pos-gap] > curose:
                    arr[pos] = arr[pos-gap]
                    pos -= gap
                arr[pos] = curose
    return arr


def random_sequence(n):
    org_list = list(range(n))
    random_list = []
    for i in range(n):
        curose = random.choice(org_list)
        org_list.remove(curose)
        random_list.append(curose)
    return random_list


if __name__ == "__main__":
    test_arr = random_sequence(1000)
    sorted_arr = shell_sort(test_arr)
    print(sorted_arr)
