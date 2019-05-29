import numpy as np
from matplotlib import pyplot as plt
import cv2


def preprocess(input):
    n = input.shape[0]
    input = np.c_[input, np.ones(n)]
    return input


def train(input, w, delta=1, flag=True):
    count = 0
    for i in input:
        tmp = np.dot(i, w.T)
        if tmp[count % 3] > tmp[(count + 1) % 3] and tmp[count % 3] > tmp[(count + 2) % 3]:
            count = (count + 1) % 3
            continue
        else:
            flag = False
            w[count % 3] += delta * i
            w[(count + 1) % 3] -= delta * i
            w[(count + 2) % 3] -= delta * i
            count = (count + 1) % 3
    return w, flag


def do_train(input, w, delta=1, flag=True):
    w, flag = train(input, w)
    while 1:
        if flag == True:
            break
        else:
            w, flag = train(input, w)
    return w


input = np.array([
    [-1, -1],
    [0, 0],
    [1, 1]
])
plt.scatter(input[:,0],input[:,1],c= ['r','g','b'])
plt.xlabel('x1')
plt.ylabel('x2')
W = np.array([
    [0, 0, 0],
    [0, 0., 0],
    [0, 0, 0]
])
input = preprocess(input)
W = do_train(input, W)
for i in W:
    if i[0] == 0 and i[1] == 0 and i[2] == 0:
        continue
    x = np.arange(-2,2,0.05)
    y = -(i[0] / i[1]) * x - i[2] / i[1]
    plt.plot(x,y)
plt.show()
