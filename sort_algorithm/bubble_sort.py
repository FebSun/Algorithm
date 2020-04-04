#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 9:12
# @Author  : FebSun
# @FileName: bubble_sort.py
# @Software: PyCharm

# 冒泡算法：
#     第一次循环：从头到尾一次便利，比较相邻的元素，大数往后移，遍历length-1次，最大数在后面。
#     第二次循环：从头到倒数第一个依次遍历比较，次数为length-2
#     .
#     .
#     最后依次遍历：从头到第二个元素，次数为1
#     总计遍历length-1次


def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__=="__main__":
    test_arr = [7, 4, 2, 5, 6, 3, 9, 1, 11, 8, 15, 10, 13, 12, 14]
    sorted_arr = bubble_sort(test_arr)
    print(sorted_arr)
