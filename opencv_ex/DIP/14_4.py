import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../image/test8.jpg')
# ch 代表顏色值，0, 1, 2
rows, cols, ch = img.shape
img1 = cv2.imread('../image/test.jpg')
rows1, cols1, ch1 = img1.shape

# 設定三個點，設兩個變數取點的變化
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))
dst1 = cv2.warpAffine(img1, M, (cols, rows))

# (221) 為  2x2 張圖的第 1 張
plt.subplot(221), plt.imshow(img), plt.title('Input')
plt.subplot(222), plt.imshow(dst), plt.title('Output')
plt.subplot(223), plt.imshow(img1), plt.title('Input')
plt.subplot(224), plt.imshow(dst1), plt.title('Output')
plt.show()
