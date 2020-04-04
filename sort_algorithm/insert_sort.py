#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 10:14
# @Author  : FebSun
# @FileName: insert_sort.py
# @Software: PyCharm

# 插入排序：
#     原理类似于打牌时候的排列排序，左边是排序好的序列，右边是未排序的序列，从右边选择第一个，插入到左边比他大的牌前面。
#     1   4   8   10  |   5   2   6   3   7
#
#     1   4   5   8   10  |   2   6   3   7
#     即10、8向后移一位，5放到空出来的位置上


def insert_sort(arr):
    length = len(arr)
    for i in range(length-1):
        # 选中的未排序右半序列的第一个数
        curose = arr[i]
        # 左侧已排序序列的最后一个数的下标
        pos = i
        while pos > 0 and arr[pos-1] > curose:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = curose
    return arr


if __name__ == "__main__":
    test_arr = [7, 4, 2, 5, 6, 3, 9, 1, 11, 8, 15, 10, 13, 12, 14]
    sorted_arr = insert_sort(test_arr)
    print(sorted_arr)
