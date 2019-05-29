import numpy as np


# 计算矩阵X的复合
def fuhe(x):
    row = x.shape[0]
    col = x.shape[1]
    res = np.zeros_like(x) * -1
    for i in range(row):
        for j in range(col):
            tmp = 0
            a = x[i]  # 第i行
            b = x[:, j]  # 第j列
            for k in range(len(a)):
                res[i][j] = max(min(a[k], b[k]), res[i][j])
    return res


def is_mohudengjia(x):
    # 先判断是不是自反
    for i in range(len(x[0])):
        if x[i][i] == 0:
            return False

    # 再判断是不是对称
    for i in range(len(x[0])):
        for j in range(len(x)):
            if x[i][j] != x[j][i]:
                return False
    # 再判断是不是传递关系
    xx = fuhe(x)
    for i in range(len(x[0])):
        for j in range(len(x)):
            if xx[i][j] > x[i][j]:
                return False
    return True


def dongtaijulei(x, theta):
    y = np.zeros_like(x)
    index = []
    for i in range(len(x[0])):
        for j in range(len(x)):
            if x[i][j] < theta:
                y[i][j] = 0
            else:
                y[i][j] = 1
    for i in range(len(y[0])):
        tmp = []
        for j in range(len(y)):
            if i == j:
                continue
            if y[i][j] == 1:
                tmp.append(j)
        if tmp != []:
            tmp.append(i)
        tmp = sorted(tmp)
        if tmp not in index:
            index.append(tmp)
    print('入=' + str(theta) + ':')
    for it in index:
        if it == []:
            continue
        print('{', end=' ')
        for i in it:
            print('x' + str(i + 1), end=' ')
        print('}')


x = np.array([
    [1, 0.1, 0.8, 0.5, 0.3],
    [0.1, 1, 0.1, 0.2, 0.4],
    [0.8, 0.1, 1, 0.3, 0.1],
    [0.5, 0.2, 0.3, 1, 0.6],
    [0.3, 0.4, 0.1, 0.6, 1]
])
lists = [0.8, 0.6, 0.5, 0.4]
if is_mohudengjia(x):
    print("是模糊等价矩阵")
else:
    print("是模糊相似矩阵")
    while (not is_mohudengjia(x)):
        x = fuhe(x)
    for i in lists:
        dongtaijulei(x, i)
