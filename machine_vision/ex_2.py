import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def op_add():
    filename = "lenna.jpg"
    img_1 = cv.imread(filename)
    plt.subplot(121)
    plt.imshow(cv.cvtColor(img_1,cv.COLOR_BGR2RGB))
    plt.title('src')
    _add = np.ones(img_1.shape, dtype='uint8') * 100
    res_img = cv.add(img_1, _add)
    plt.subplot(122)
    plt.imshow(cv.cvtColor(res_img, cv.COLOR_BGR2RGB))
    plt.title('res')
    plt.show()


def op_substract():
    filename = "lenna.jpg"
    img_1 = cv.imread(filename)
    plt.subplot(121)
    plt.imshow(cv.cvtColor(img_1, cv.COLOR_BGR2RGB))
    plt.title('src')
    _sub = np.ones(img_1.shape, dtype='uint8') * 55
    res_img = cv.subtract(img_1, _sub)
    plt.subplot(122)
    plt.imshow(cv.cvtColor(res_img, cv.COLOR_BGR2RGB))
    plt.title('res')
    plt.show()


def op_multiply():
    filename = "lenna.jpg"
    img_1 = cv.imread(filename)
    plt.subplot(121)
    plt.imshow(cv.cvtColor(img_1, cv.COLOR_BGR2RGB))
    plt.title('src')
    _mul = np.ones(img_1.shape, dtype='uint8') * 9
    res_img = cv.multiply(img_1, _mul)
    plt.subplot(122)
    plt.imshow(cv.cvtColor(res_img, cv.COLOR_BGR2RGB))
    plt.title('res')
    plt.show()


def op_divide():
    filename = "lenna.jpg"
    img_1 = cv.imread(filename)
    plt.subplot(121)
    plt.imshow(cv.cvtColor(img_1, cv.COLOR_BGR2RGB))
    plt.title('src')
    _div = np.ones(img_1.shape, dtype='uint8') * 7
    res_img = cv.divide(img_1, _div)
    plt.subplot(122)
    plt.imshow(cv.cvtColor(res_img, cv.COLOR_BGR2RGB))
    plt.title('res')
    plt.show()


def op_pingyi():
    file_name = 'lenna.jpg'
    image = cv.imread(file_name)
    plt.subplot(131)
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.title('src')
    M = np.float32([[1, 0, 25], [0, 1, 50]])  # 平移矩阵1：向x正方向平移25，向y正方向平移50
    shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
    plt.subplot(132)
    plt.imshow(cv.cvtColor(shifted, cv.COLOR_BGR2RGB))
    plt.title('res1')
    M = np.float32([[1, 0, -50], [0, 1, -90]])  # 平移矩阵2：向x负方向平移-50，向y负方向平移-90
    shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
    plt.subplot(133)
    plt.imshow(cv.cvtColor(shifted, cv.COLOR_BGR2RGB))
    plt.title('res2')
    plt.show()


def op_xuanzhuan():
    file_name = 'lenna.jpg'
    image = cv.imread(file_name)
    plt.subplot(131)
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.title('src')
    (h, w) = image.shape[:2]
    center = (h / 2, w / 2)
    M = cv.getRotationMatrix2D(center, 45, 0.5)  # 顺时针旋转75 缩放为0.5
    res_1 = cv.warpAffine(image, M, (w, h))
    plt.subplot(132)
    plt.imshow(cv.cvtColor(res_1, cv.COLOR_BGR2RGB))
    plt.title('res1')
    M = cv.getRotationMatrix2D(center, -30, 1.4) # 逆时针旋转30 放大为1.4
    res_2 = cv.warpAffine(image, M, (w, h))
    plt.subplot(133)
    plt.imshow(cv.cvtColor(res_2, cv.COLOR_BGR2RGB))
    plt.title('res2')
    plt.show()


def op_fanzhuan():
    file_name = 'lenna.jpg'
    image = cv.imread(file_name)
    plt.subplot(221)
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.title('src')
    f_1 = cv.flip(image, 1)  # 水平翻转
    f_2 = cv.flip(image, 0) # 垂直翻转
    f_3 = cv.flip(image, -1) # 原点翻转
    f_1 = cv.cvtColor(f_1, cv.COLOR_BGR2RGB)
    f_2 = cv.cvtColor(f_2, cv.COLOR_BGR2RGB)
    f_3 = cv.cvtColor(f_3, cv.COLOR_BGR2RGB)
    plt.subplot(222)
    plt.imshow(f_1)
    plt.title('水平')
    plt.subplot(223)
    plt.imshow(f_2)
    plt.title('垂直')
    plt.subplot(224)
    plt.imshow(f_3)
    plt.title('原点')
    plt.show()


op_pingyi()
op_xuanzhuan()
op_fanzhuan()
op_add()
op_substract()
op_multiply()
op_divide()
