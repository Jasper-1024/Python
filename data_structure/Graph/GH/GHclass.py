#!/usr/bin/python3


# 图的基类
class GH(object):
    # v 个顶点的图
    def __init__(self, v):
        pass

    # 顶点数
    def rV(self):
        pass

    # 边数
    def rE(self):
        pass

    # 添加边 v-m
    def addEdge(self, v, e):
        pass

    # 返回v相邻的所有顶点
    def adjlist(self, v):
        pass

    # 反向图 (有向图)
    def reverse(self):
        pass

    # 字符串
    def toString(self):
        pass

    # save to file
    def save(self):
        pass

    # load from file
    def load(self, file):
        pass
