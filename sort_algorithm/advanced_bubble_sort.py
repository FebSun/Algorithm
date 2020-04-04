#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 9:27
# @Author  : FebSun
# @FileName: advanced_bubble_sort.py
# @Software: PyCharm


# 冒泡算法进阶：
#     加上flag，若一次循环没有元素的变动，则结束循环


def advanced_bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        flag = True
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break
    return arr


if __name__ == "__main__":
    test_arr = [7, 4, 2, 5, 6, 3, 9, 1, 11, 8, 15, 10, 13, 12, 14, 17, 18, 19]
    sorted_arr = advanced_bubble_sort(test_arr)
    print(sorted_arr)
