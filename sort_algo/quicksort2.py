#!/usr/bin/env python
# -*- coding:utf8 -*-

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class QuickSort(object):
    def __init__(self, datas):
        self.datas = datas
        self.flag = Stack()

    def _sort(self, left, right):
        self.flag.push(left)
        self.flag.push(right)
        while not self.flag.isEmpty():
            r = self.flag.pop()  # 右边界
            l = self.flag.pop()  # 左边界
            i = l
            j = r
            temp = self.datas[l]
            while i != j:
                while self.datas[j] >= temp and i < j:
                    j -= 1

                while self.datas[i] <= temp and i < j:
                    i += 1

                if i < j:
                    self.datas[i], self.datas[j] = \
                            self.datas[j], self.datas[i]

                self.datas[l], self.datas[i] = self.datas[i], temp

            if not l >= i-1:
                self.flag.push(l)
                self.flag.push(i-1)

            if not i+1 >= r:
                self.flag.push(i+1)
                self.flag.push(r)

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
