#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 21:10
# @Author  : FebSun
# @FileName: heap_sort.py
# @Software: PyCharm

from collections import deque
import random
# 堆排序：
#     1、将一个无序的序列生成一个最大堆
#     2、将堆顶元素与堆的最后一个元素对换位置
#     3、替换后，调整序列为最大堆
#     4、重复上述过程直到只剩下最后一个元素


def heap_sort(arr):
    # 因为在序列头部增加了一个辅助位，所以长度需要减一
    length = len(arr) - 1
    # 从最下部的根节点进行递归调整
    sort_count = length // 2
    for i in range(sort_count):
        heap_adjust(arr, sort_count-i, length)

    # 交换堆顶与堆底部的元素，即将最大的元素放到尾部
    # 交换后进行调整
    for i in range(length - 1):
        arr[1], arr[length - i] = arr[length - i], arr[1]
        heap_adjust(arr, 1, length - i - 1)
    print(arr)
    return [arr[i] for i in range(1, length + 1)]


def heap_adjust(arr, start, end):
    i = start
    j = 2 * i
    temp = arr[i]
    while j <= end:
        # 精简下条件，原先的太二了
        # if j <= end and j+1 <= end and arr[j] < arr[j+1]:

        # 选取根节点下面的叶子结点中较大的一个
        if j < end and arr[j] < arr[j + 1]:
            j = j + 1
        # 比较跟节点与较大的叶子结点，两个进行替换
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i = j
            j = 2 * i
        else:
            break


if __name__ == "__main__":
    test_arr = list(range(1, 50))
    random.shuffle(test_arr)
    # 节点编号是从0 开始的，因为叶子结点是2i, 2i+1，节点从1计算比较方便，所以需要在序列头部添加一个辅助位
    # deque为双向数列
    test_arr = deque(test_arr)
    test_arr.appendleft(0)
    sorted_arr = heap_sort(test_arr)
    print(sorted_arr)
