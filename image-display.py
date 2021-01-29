
import cv2
import numpy as np
# 安裝 matplotlib 套件
from matplotlib import pyplot as plt

# 函數 cv2.imreaad 讀取圖像，檔案路徑後，0 代表灰黑白，1 代表彩色
img = cv2.imread('./cat.jpg', 1)

# 切塊置換[y2:y1, x2:x1]
# roi = img[400:1500, 1300:2800]
# img[500:1600, 0:1500] = roi

px = img[100, 100] = [0, 0, 0]
print(px)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 檢查是否有讀到圖
print(img.shape, img.size)

# matplotlib 套件指令
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# cv2.namedWindow('cat', cv2.WINDOW_NORMAL)

# # 函數 cv2.imshow 顯示圖像，第一參數「視窗名稱」，第二參數「變數」
# cv2.imshow('cat', img)

# # 函數 cv2.imwrite 儲存圖像，第一參數「圖像名稱」，第二參數「參數」
# cv2.imwrite('blackcat.jpg', img)
# cv2.waitKey(0)
# # 函數 cv2.destroyAllwindoes 關閉任意視窗
# cv2.destoryAllwindows()
