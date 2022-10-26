# 批量生成aruco标记
import cv2
import numpy as np
# 生成aruco标记
# 加载预定义的字典
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# 在armark文件夹下会生成一系列的6*6 aruco标记
markerImage = np.zeros((200, 200), dtype=np.uint8)
for i in range(30):
    markerImage = cv2.aruco.drawMarker(dictionary, i, 200, markerImage, 1)

    firename='armark/'+str(i)+'.png'
    cv2.imwrite(firename, markerImage)
