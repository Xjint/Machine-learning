import cv2 as cv
import  numpy as np
from matplotlib import pyplot as plt

filename = '2.jpg'
img = cv.imread(filename)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()