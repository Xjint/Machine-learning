import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def trans_1(i):
    if i < 0.35:
        y = 0.3 * i
    elif 0.35 <= i <= 0.65:
        y = 0.105 + 2.6333 * (i - 0.35)
    else:
        y = 1 + 0.3 * (i - 1)
    return y


def trans_2(i):
    if i <= 0.5:
        y = 15.9744 * (i ** 5)
    else:
        y = (i - 0.5) ** 0.2 + 0.12
    return y


def trans_3(i , a):
    return i ** a


def trans_last(i):
    if i >= 0.2 and i <= 0.4:
        i = 0.6
    return i


def do_t1():
    filename = "pic/Fig3.10(b).jpg"
    src_img = cv.imread(filename)
    grey_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    copy_img = grey_img.copy()
    rows = copy_img.shape[0]
    cols = copy_img.shape[1]

    for i in range(rows):
        for j in range(cols):
            copy_img[i][j] = trans_1(grey_img[i][j] / 255) * 255
    copy_img = cv.cvtColor(copy_img, cv.COLOR_BGR2RGB)
    x = np.arange(0, 1, 0.01)
    y = []
    for i in x:
        y.append(trans_1(i))
    plt.figure()
    plt.subplot(231)
    plt.imshow(cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB))
    plt.subplot(232)
    plt.plot(x, y)
    plt.subplot(233)
    plt.imshow(copy_img)
    for i in range(rows):
        for j in range(cols):
            copy_img[i][j] = trans_2(grey_img[i][j] / 255) * 255
    copy_img = cv.cvtColor(copy_img, cv.COLOR_BGR2RGB)
    x = np.arange(0, 1, 0.01)
    y = []
    for i in x:
        y.append(trans_2(i))
    plt.subplot(234)
    plt.imshow(cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB))
    plt.subplot(235)
    plt.plot(x, y)
    plt.subplot(236)
    plt.imshow(copy_img)
    plt.show()
    plt.show()


def do_t3():
    filename = "pic/Fig3.08(a).jpg"
    src_img = cv.imread(filename)
    grey_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    copy_img = grey_img.copy()
    rows = copy_img.shape[0]
    cols = copy_img.shape[1]

    for i in range(rows):
        for j in range(cols):
            copy_img[i][j] = trans_3(grey_img[i][j] / 255, 0.6) * 255
    copy_img = cv.cvtColor(copy_img, cv.COLOR_BGR2RGB)
    x = np.arange(0, 1, 0.01)
    y = []
    for i in x:
        y.append(trans_3(i, 0.6))
    plt.figure()
    plt.subplot(331)
    plt.imshow(cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB))
    plt.subplot(332)
    plt.plot(x, y)
    plt.subplot(333)
    plt.imshow(copy_img)
    for i in range(rows):
        for j in range(cols):
            copy_img[i][j] = trans_3(grey_img[i][j] / 255, 0.4) * 255
    copy_img = cv.cvtColor(copy_img, cv.COLOR_BGR2RGB)
    x = np.arange(0, 1, 0.01)
    y = []
    for i in x:
        y.append(trans_3(i, 0.4))
    plt.subplot(334)
    plt.imshow(cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB))
    plt.subplot(335)
    plt.plot(x, y)
    plt.subplot(336)
    plt.imshow(copy_img)
    for i in range(rows):
        for j in range(cols):
            copy_img[i][j] = trans_3(grey_img[i][j] / 255, 0.3) * 255
    copy_img = cv.cvtColor(copy_img, cv.COLOR_BGR2RGB)
    x = np.arange(0, 1, 0.01)
    y = []
    for i in x:
        y.append(trans_3(i, 0.3))
    plt.subplot(337)
    plt.imshow(cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB))
    plt.subplot(338)
    plt.plot(x, y)
    plt.subplot(339)
    plt.imshow(copy_img)
    plt.show()


def neg_trans():
    filename = "pic/Fig3.04(a).jpg"
    src_img = cv.imread(filename)
    src_img = cv.cvtColor(src_img, cv.COLOR_BGR2RGB)
    res_img = 1 - src_img
    plt.subplot(121)
    plt.imshow(src_img)
    plt.title('input')
    plt.subplot(122)
    plt.imshow(res_img)
    plt.title('output')
    plt.show()


def do_last():
    filename = "pic/Fig3.10(b).jpg"
    src_img = cv.imread(filename)
    grey_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    copy_img = grey_img.copy()
    rows = copy_img.shape[0]
    cols = copy_img.shape[1]

    for i in range(rows):
        for j in range(cols):
            copy_img[i][j] = trans_last(grey_img[i][j] / 255) * 255
    copy_img = cv.cvtColor(copy_img, cv.COLOR_BGR2RGB)
    x = np.arange(0, 1, 0.01)
    y = []
    for i in x:
        y.append(trans_last(i))
    plt.figure()
    plt.subplot(131)
    plt.imshow(cv.cvtColor(grey_img, cv.COLOR_GRAY2RGB))
    plt.subplot(132)
    plt.plot(x, y)
    plt.subplot(133)
    plt.imshow(copy_img)
    plt.show()


do_t1()
do_t3()
neg_trans()
do_last()

