import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


filename = 'pic/Fig3.41(c).jpg'
src_img = cv.imread(filename, 0)
plt.subplot(321)
plt.title('src')
plt.imshow(src_img, plt.cm.gray)

sobel = np.array([[-1,-2,-1],
                  [0,0,0],
                  [1,2,1]])
laplacian = np.array([[1,1,1],
                     [1,-8,1],
                     [1,1,1]])
unsharp_masking = np.array([
    [1,1,1],
    [1,-9,1],
    [1,1,1]])
A = -1
high_boost_filtering = np.array([[1,1,1],
                                 [1,-A-8,1],
                                 [1,1,1]])

img_1 = cv.filter2D(src_img,-1,sobel)
img_1 = cv.add(src_img, img_1)
plt.subplot(322)
plt.title('sobel')
plt.imshow(img_1, plt.cm.gray)

img_2 = cv.filter2D(src_img,-1,laplacian)
img_2 = cv.add(src_img, img_2)
plt.subplot(323)
plt.title('laplacian')
plt.imshow(img_2, plt.cm.gray)

img_3 = cv.filter2D(src_img,-1,unsharp_masking)
img_3 = cv.add(src_img, img_3)
plt.subplot(324)
plt.title('unsharp')
plt.imshow(img_3, plt.cm.gray)

img_4 = cv.filter2D(src_img,-1,high_boost_filtering)
img_4 = cv.add(src_img, img_4)
plt.subplot(325)
plt.title('high')
plt.imshow(img_4, plt.cm.gray)




plt.show()