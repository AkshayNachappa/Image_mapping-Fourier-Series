import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('ball.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(img,100,200)
plt.subplot(2,2,1),plt.imshow(img,cmap='hot')
plt.title('Color'),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(gray,cmap = 'gray')
plt.title('Gray'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
