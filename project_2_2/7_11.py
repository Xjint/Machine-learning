# -*- coding: utf-8 -*-
import numpy  as np
import sklearn.datasets as ds
import matplotlib.pyplot as plt
import random
import math
import operator

SAMPLE_NUM = 200  # 样本数量
FEATURE_NUM = 2  # 每个样本的特征数量
CLASS_NUM = 2  # 分类数量

# 1. 初始化测试数据
sample, y = ds.make_blobs(SAMPLE_NUM, n_features=FEATURE_NUM, centers=CLASS_NUM, random_state=3)

sim_array = [[0 for col in range(SAMPLE_NUM)] for row in range(SAMPLE_NUM)]

tree_node = []  # 选择的节点
path_node = []  # 路径
value_node = []  # 存储路径对应的值


def _build_kruskal_tree():
    # kruskal每次筛选与当前已选区域联通的点，将满足要求最好的点加入已选区域

    tree_node.append(0)

    while len(tree_node) < SAMPLE_NUM:

        tmp_sum = 0
        tmp_set = (0, 0)
        tmp_node = 0

        for node in tree_node:

            for i in range(0, SAMPLE_NUM):

                if node == i:

                    continue

                else:

                    if i in tree_node:

                        continue

                    else:

                        # 计算距离
                        if sim_array[node][i] > tmp_sum:
                            tmp_sum = sim_array[node][i]

                            tmp_set = (node, i)

                            tmp_node = i

        path_node.append(tmp_set)
        tree_node.append(tmp_node)
        value_node.append((len(path_node), tmp_sum))


def _do_fuzzy_cluster():
    # 2. 构造相似矩阵

    max = 0

    for i in range(0, SAMPLE_NUM):

        for j in range(0, SAMPLE_NUM):

            if i == j:

                sim_array[i][j] = 1

            else:

                tmp = 0

                for k in range(0, FEATURE_NUM):
                    tmp += sample[i][k] * sample[j][k]

                sim_array[i][j] = tmp

                if tmp > max:
                    max = tmp

    for i in range(0, SAMPLE_NUM):

        for j in range(0, SAMPLE_NUM):

            if i != j:
                sim_array[i][j] = sim_array[i][j] / max

    # 3. 构造最大树
    _build_kruskal_tree()

    # 4. 聚类划分并显示
    # 根据最大生成树来进行分类
    value_node.sort(key=operator.itemgetter(1))

    gamma = value_node[int(len(value_node) / 2)][1]

    # 根据这个gamma值分开
    y_pre = [0 for col in range(SAMPLE_NUM)]

    for i in range(0, SAMPLE_NUM - 1):

        start = path_node[i][0]
        end = path_node[i][1]

        if value_node[i][1] > gamma:

            y_pre[start] = 1
            y_pre[end] = 1

        else:
            y_pre[start] = 0
            y_pre[end] = 0

    # print(np.array(y_pre))
    # print(y)

    # 显示

    plt.figure(figsize=(5, 6), facecolor='w')
    plt.subplot(211)
    plt.title('origin classfication')
    plt.scatter(sample[:, 0], sample[:, 1], c=y, s=20, edgecolors='none')

    plt.subplot(212)
    plt.title('fuzzy classfication')
    plt.scatter(sample[:, 0], sample[:, 1], c=np.array(y_pre), s=20, edgecolors='none')

    plt.show()


"""
说明：

模糊聚类的代码实现，基于最大树算法，针对笔记《模糊聚类分析》

作者：fredric

日期：2018-12-23

"""
if __name__ == "__main__":
    _do_fuzzy_cluster()


