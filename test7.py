import cv2
import numpy as np
from matplotlib import pyplot as plt

# 兩張圖合併

img = cv2.imread('./cat.jpg', 1)
b = cv2.imread('./cat.jpg', 1)
img1 = b[500:1000, 100:1300]
img2 = b[700:1200, 300:1500]

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
b[700:1200, 300:1500] = dst


plt.imshow(dst)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
