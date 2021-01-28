import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)


cv2.line(img, (0, 0), (500, 500), (255, 0, 0), 5)

cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 3)

cv2.circle(img, (200, 200), 100, (0, 0, 255), 3)

# 描繪多邊形
# boolean true 為自動封閉圖案，false 為點到為止，integer 32 位元
points = np.array([[150, 150], [100, 100], [100, 300]], np.int32)
cv2.polylines(img, [points], 1, (0, 150, 150), 5)

cv2.ellipse(img, (150, 150), (250, 150), 0, 0, 360, (255, 150, 0), 5)

# 描繪文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Aloha!", (100, 100), font, 2, (255, 255, 255), 5)


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
