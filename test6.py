import cv2
import numpy as np
from matplotlib import pyplot as plt

# 讀取特定顏色，或變換指定顏色
img = cv2.imread('./cat.jpg', 1)
b = cv2.imread('./cat.jpg', 1)
b[100:200, 100:200, 0] = 0
b[300:500, 600:800, 1] = 0
b[500:600, 300:1000, 2] = 0

plt.imshow(b)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
