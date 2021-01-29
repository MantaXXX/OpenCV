import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # 獲取每一幀
    ret, frame = cap.read()
# 換到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 定蓝色的值
    lower_blue = np.array([50, 50, 50])
    upper_blue = np.array([130, 255, 255])

# 根据值構建遮罩
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
# 對原圖像和遮罩位算
    res = cv2.bitwise_and(frame, frame, mask=mask)
# 顯示圖像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
# 關閉視窗
cv2.destroyAllWindows()
