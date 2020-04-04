#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 9:39
# @Author  : FebSun
# @FileName: select_sort.py
# @Software: PyCharm

# 选择排序：
#     1、从未排序的序列中选出最小的元素，存放在排序列表的首位
#         此时arr[min]与arr[0]交换顺序
#     2、从未排序的序列中选出最小的元素，存放在排序列表的末尾
#         此时arr[min]与arr[1]交换顺序
#         .
#         .
#     n、第n次，将最小的元素与arr[n]交换顺序

# 错误的方案：
#     新建一个列表作为有序列表，从原列表中找到该元素，然后删除，再在新列表末尾添加
#     存在以下问题：
#         1、需要使用remove()方法。remove()方法会删除与数值相同的第一个元素，不建议使用remove。
#         2、需要频繁的删除，增加列表长度，资源消耗比较大，不如简单的替换效率高。


def select_sort(arr):
    length = len(arr)
    for i in range(length-1):
        # 先将arr[i]作为最小值，然后从arr[i+1]进行遍历，遍历到末尾，找出最小的元素
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    test_arr = [7, 4, 2, 5, 6, 3, 9, 1, 11, 8, 15, 10, 13, 12, 14]
    sorted_arr = select_sort(test_arr)
    print(sorted_arr)