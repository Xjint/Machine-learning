import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


filename = 'pic/Fig3.20(a).jpg'
src_img = cv.imread(filename, 0)
copy_img = src_img.copy()
rows = copy_img.shape[0]
cols = copy_img.shape[1]
plt.subplot(321)
plt.hist(src_img.ravel(), 256, [0,256])

plt.subplot(322)
plt.imshow(src_img, plt.cm.gray)

res = cv.equalizeHist(src_img)

plt.subplot(323)
plt.hist(res.ravel(), 256, [0, 256])

plt.subplot(324)
plt.imshow(res, plt.cm.gray)
y = []
for i in range(255):
    if i <= 5:
         y.append(1400 * i)
    elif i > 5 and i <= 20:
         y.append(7000 - 310 * i)
    elif i > 20 and i <= 180:
         y.append(900 - 5 * i)
    elif  i > 180 and i <= 225:
        y.append(-1440 + 8 * i)
    else:
        y.append(3060 -12 * i)
n = np.array(y)
res_img = cv.equalizeHist(src_img, n)

plt.subplot(325)
plt.hist(res_img.ravel(), 256, [0, 256])

plt.subplot(326)
plt.imshow(res_img, plt.cm.gray)
plt.show()