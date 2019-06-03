import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


filename = 'pic/Fig5.10(a).jpg'
src_img = cv.imread(filename, 0)
plt.subplot(131)
plt.title('src')
plt.imshow(src_img, plt.cm.gray)

mean_img = src_img.copy()
kernel = np.ones((3,3)) / 9
mean_img = cv.filter2D(src_img,-1,kernel)
plt.subplot(132)
plt.title('mean')
plt.imshow(mean_img, plt.cm.gray)

median_img = src_img.copy()
median_img = cv.medianBlur(src_img, 3)
plt.subplot(133)
plt.title('median')
plt.imshow(median_img, plt.cm.gray)


plt.show()