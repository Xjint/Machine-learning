import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 对训练样本进行预处理，input_1是I类样本，Input_2是II类样本
def preprocess(input_1, input_2):
    n = input_1.shape[0]
    one = np.ones(n)
    neg = np.array([-1 for i in range(n)])
    output_1 = np.c_[input_1, one]
    output_2 = np.c_[input_2, one]
    output_2 = -1 * output_2
    return output_1, output_2


# 训练一轮的过程 返回值为迭代一轮后的w和flag  flag用于判断w是否发生变化，若flag为true说明迭代结束,delta为矫正系数
def train(input_1, input_2, w, delta=1, flag=True):
    for in_1 in input_1:
        if np.dot(w, in_1) <= 0:
            flag = False
            w += delta * in_1
    for in_2 in input_2:
        if np.dot(w, in_2) <= 0:
            flag = False
            w += delta * in_2
    return w, flag


# 控制迭代的次数
def do_train(input_1, input_2, w, delta=1, flag=True):
    w, flag = train(input_1, input_2, w)
    while 1:
        if flag == True:
            break
        else:
            w, flag = train(input_1, input_2, w)
    return w


input_1 = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0]
])
input_2 = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 1]
])
W = np.array([-1, -2., -2, 0])
output_1, output_2 = preprocess(input_1, input_2)
do_train(output_1, output_2, W)
w1 = W[0]
w2 = W[1]
w3 = W[2]
b =  W[3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(input_1[:,0],input_1[:,1],input_1[:,2],c='c')
ax.scatter(input_2[:,0],input_2[:,1],input_2[:,2],c='r')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')

x = np.arange(-1,1,0.05)
y = np.arange(-1,1,0.05)
X, Y = np.meshgrid(x, y)
Z = -(w1/w3) * X - (w2/w3) * Y - b/w3
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1)
plt.show()
