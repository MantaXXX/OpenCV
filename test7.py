import cv2
import numpy as np
from matplotlib import pyplot as plt

# 兩張圖合併

img = cv2.imread('./cat.jpg', 1)
b = cv2.imread('./cat.jpg', 1)

# 紀錄所耗時間，起始點
e1 = cv2.getTickCount()

img1 = b[500:1000, 100:1300]
img2 = b[700:1200, 300:1500]

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
b[700:1200, 300:1500] = dst

# 紀錄所耗時間，結束點
e2 = cv2.getTickCount()
# 紀錄所耗時間，兩者點相差，函數 getTickFrequency() 算出時間差
t = (e2-e1) / cv2.getTickFrequency()
print(t)

plt.imshow(dst)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
