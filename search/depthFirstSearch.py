# -*- coding:utf8 -*-
'''
简介：本程序主要简单实现深度优先搜索算法(depth first search)
      并用解决数的全排列的问题。
实现方法：递归
作者：陈栋权
2016/9/24    第一次发布
'''

class DFS(object):
    '''
    numlen: 为有几位数字，如3,则为1,2,3
    result: 用来保存个序列的结果
    book: 用来判断那个数字已经排列了
    '''
    def __init__(self, n):
        self.numlen = n
        self.result = [0 for i in range(n)]
        self.book = [0 for i in range(n)]

    def dfs(self, s):
        step = s-1
#        if step == self.numlen:
#            r = ''
#            for i in range(self.numlen):
#                r += str(self.result[i])
#
#            print r
#            return

        if step == self.numlen:
            result = self.result
            if result[0]*100+result[1]*10+result[2] + \
               result[3]*100+result[4]*10+result[5] == \
               result[6]*100+result[7]*10+result[8] and \
               result[0]*100+result[1]*10+result[2] < \
               result[3]*100+result[4]*10+result[5]:
                print "%d%d%d+%d%d%d=%d%d%d" % (result[0], result[1],
                                                result[2], result[3],
                                                result[4], result[5],
                                                result[6], result[7],
                                                result[8]
                                               )

            return

        # 用来尝试每种可能，即第step位的数为i
        for i in range(self.numlen):
            if self.book[i] == 0:
                self.result[step] = i+1
                self.book[i] = 1
                self.dfs(s+1)
                self.book[i] = 0
        return
