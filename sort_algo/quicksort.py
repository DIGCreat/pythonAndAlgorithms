#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
简介:本程序主要是用python实现快速排序，程序的功能是实现
     升序排列。
     本程序在数据量大的情况下，需要注意递归深度的问题。

作者:King  日期:2016/08/01  版本1
'''

class QuickSort(object):
    '''
    self.datas:       要排序的数据列表
    _sort():          排序函数
    show():           输出结果函数

    用法：
    QuickSort(datas)  实例化一个排序对象

    QuickSort(datas)._sort(left, right)
                      开始排序，由于排序直接操作
                      self.datas, 所以排序结果也
                      保存在self.datas中, left为
                      排序的开始位置，right为排
                      序的结束位置。因此可以实现
                      局部排序

    QuickSort(datas).show()  输出结果
    '''
    def __init__(self, datas):
        self.datas = datas

    def _sort(self, left, right):
        # 排序函数，由两个游标分别从两端开始遍历
        # 左端数据要比基数小，所以判断条件是遇到
        # 比基数大的就要停下。
        # 右端的情况与左端相反。
        #
        # 注意：程序一定要先从右端开始遍历，因为
        #       两端遍历最终停下的条件肯定是相遇
        #       的时候，如果左端先移动，则最后停
        #       下时的数值肯定比基数大，若将这个
        #       数字与基数交换，则基数左边的数字
        #       就不是全部比基数小了，程序运行就
        #       不正确了。
        if(left > right):
            return
        temp = self.datas[left]
        i = left
        j = right
        while i != j:
            while(self.datas[j] >= temp and i < j):
                j -= 1

            while(self.datas[i] <= temp and i < j):
                i += 1

            if i < j:
                self.datas[i], self.datas[j] = \
                        self.datas[j], self.datas[i]

        self.datas[left], self.datas[i] = self.datas[i], temp

        self._sort(left, i-1)
        self._sort(i+1, right)

    def show(self):
        print 'Result is:',
        for i in self.datas:
            print i,

        print ''

if __name__ == '__main__':
    try:
        datas = raw_input('Please input some number:')
        datas = datas.split()
        datas = [int(datas[i]) for i in range(len(datas))]
    except Exception:
        pass

    qs = QuickSort(datas)
    qs._sort(0, len(datas)-1)
    qs.show()
