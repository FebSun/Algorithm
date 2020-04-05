#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 14:43
# @Author  : FebSun
# @FileName: qiuick_sort.py
# @Software: PyCharm

import random
# 快速排序：
#     基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，
#         其中一部分的所有数据都比另外一部分的所有数据都要小，
#         然后再按此方法对这两部分数据分别进行快速排序，
#         整个排序过程可以递归进行，以此达到整个数据变成有序序列
#     原理：
#         1、在数列之中，选择一个元素作为“基准”（pivot）。
#         2、数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边
#         3、以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。
# 返回规则是：左边分区+基准值+右边分区


def quick_sort(arr):
    length = len(arr)
    # 这么写存在BUG，拆分下去，会存在[n]、[]这两种情况
    # 若只有length == 1的判断，[]场景将会造成异常
    # if length == 1:
    if length < 2:
        return arr
    piovt = arr[0]
    left = []
    right = []
    for i in range(1, length):
        if arr[i] > piovt:
            right.append(arr[i])
        else:
            left.append(arr[i])
    # [piovt]，这里需要特别注意，因为左右都是列表，所以必须将piovt也作为列表包装起来
    return quick_sort(left) + [piovt] + quick_sort(right)


if __name__ == "__main__":
    test_arr = list(range(500))
    random.shuffle(test_arr)
    sorted_arr = quick_sort(test_arr)
    print(sorted_arr)
