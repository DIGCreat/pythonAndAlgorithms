#!/usr/bin/env python
#-*- coding:utf8 -*-

class BucketSort(object):
    '''
    self.datas:       要排序的数据列表
    self.bucketSize:  水桶的大小(数据集的范围，如bucketSize=10,
                      则表示数据集的范围为0-9)
    self.result:      保存排序后的结果
    self.bucket:      代表水桶，指数据集内的所有元素
    _sort():          排序函数
    show():           输出结果的函数

    用法：
    BucketSort(datas, size)   或者BucketSort(datas)，size的默认值为100

    BucketSort(datas)._sort() 这样就是开始排序
    BucketSort(datas).show()  这样就可以把排序后的结果输出
    '''
    def __init__(self, datas, size=100):
        self.datas = datas
        self.bucketSize = size
        self.result = [0 for i in range(len(datas))]
        self.bucket = [0 for i in range(self.bucketSize)]

    def _sort(self):
        # 读入各个元素，并在对应的位置统计，当bucket里的元素不为0
        # 就保存到result里面
        for num in self.datas:
            self.bucket[num] += 1
        j = 0
        for i in range(self.bucketSize):
            while(self.bucket[i]):
                self.result[j] = i
                self.bucket[i] -= 1
                j += 1

    def show(self):
        print "Resutl is:",
        for i in self.result:
            print i,
        print ''


if __name__ == '__main__':
    try:
        size = raw_input("Please input size(default=100):")
        if size:
            size = int(size)
        datas = raw_input('Please input some number:')
        datas = datas.split()
        datas = [int(datas[i]) for i in range(len(datas))]
    except Exception:
        pass
    if size:
        bks = BucketSort(datas, size)
    else:
        bks = BucketSort(datas)
    bks._sort()
    bks.show()
