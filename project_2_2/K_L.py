import numpy as np
from matplotlib import pyplot as plt


# 计算总体自相关矩阵R
def rov(x):
    sum = np.array([[0, 0], [0, 0]])
    for i in range(len(x[0])):
        tmp = np.array([x[0][i], x[1][i]]).reshape(-1, 1)
        sum = sum + tmp * tmp.T
    sum = sum / len(x[0])
    return sum


X = [[-5, -5, -4, -5, -6, 5, 5, 5, 4],
     [-5, -4, -5, -6, -5, 5, 6, 4, 5]
     ]
targer_X = np.array(X)
plt.figure()
plt.subplot(121)
plt.scatter(targer_X[0][:5], targer_X[1][:5], label='w1')
plt.scatter(targer_X[0][5:], targer_X[1][5:], label='w2')
plt.legend()
rov_x = rov(targer_X)
# a记录的是特征值 b记录的是特征值对应的特征向量
# 这个特征向量是已经经过归一化的 特征向量是按列存放的
a, b = np.linalg.eig(rov_x)
# 对特征向量进行排序 下面这个变量存放的是下标
sorted_a = np.argsort(a)
print(b)
# max_b即为要找的特征向量
max_b = b[:, sorted_a[:-2:-1]]
s = np.zeros_like(X[0], dtype=float)
sy = np.zeros_like(s)
for i in range(len(X[0])):
    tmp = np.array([X[0][i], X[1][i]]).reshape(-1, 1)
    s[i] = max_b.T.dot(tmp)
print(s)
plt.subplot(122)
plt.scatter(s[:5], sy[:5], label='w1')
plt.scatter(s[5:], sy[5:], label='w2')
plt.legend()
frame = plt.gca()
# y 轴不可见
frame.axes.get_yaxis().set_visible(False)
plt.show()
