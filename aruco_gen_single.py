#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
# 生成aruco标记
# 加载预定义的字典

# 会加载cv2.aruco.DICT_6X6_250包含250个标记的字典，其中每个标记都是6×6位二进制模式
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# 生成标记
markerImage = np.zeros((200, 200), dtype=np.uint8)

# 第二个参数22是aruco的标记id（0～249），
# 第三个参数决定生成的标记的大小，在上面的示例中，它将生成200×200像素的图像，
# 第四个参数表示将要存储aruco标记的对象(上面的markerImage）
# 第五个参数是边界宽度参数，它决定应将多少位（块）作为边界添加到生成的二进制图案中。
markerImage = cv2.aruco.drawMarker(dictionary, 22, 200, markerImage, 1)
cv2.imwrite("marker22.png", markerImage)

