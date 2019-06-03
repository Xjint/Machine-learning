import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


filename = 'pic/Fig3.24.jpg'
src_img = cv.imread(filename, 0)
mean_img = src_img.copy()
plt.subplot(221)
plt.imshow(src_img,plt.cm.gray)

# kernel = np.ones((3,3)) / 9
# mean_img = cv.filter2D(src_img,-1,kernel)
mean_img = cv.blur(src_img,(3,3))
plt.subplot(222)
plt.imshow(mean_img,plt.cm.gray)
plt.show()
mean = cv.mean(src_img)[0]
(mean, std) = cv.meanStdDev(src_img)






