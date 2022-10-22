import numpy as np
import time
import cv2
import cv2.aruco as aruco

# 读取图片
frame = cv2.imread('IMG_3739.jpg')
# 调整图片大小
frame = cv2.resize(frame, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
# 灰度话
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 设置预定义的字典
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
# 使用默认值初始化检测器参数
parameters = aruco.DetectorParameters_create()
# 使用aruco.detectMarkers()函数可以检测到marker，返回ID和标志板的4个角点坐标
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
# 画出标志位置
aruco.drawDetectedMarkers(frame, corners, ids)

cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()




# 对于每次成功检测到标记，将按从左上，右上，右下和左下的顺序检测标记的四个角点。在Python中，它们存储为Numpy 数组。
# detectMarkers()函数用于检测和确定标记角点的位置。
#
# 第一个参数image是带有标记的场景图像。
# 第二个参数dictionary是用于生成标记的字典。成功检测到的标记将存储在markerCorners中，其ID存储在markerIds中。先前初始化的DetectorParameters对象作为传递参数。
# 第三个参数parameters： DetectionParameters 类的对象，该对象包括在检测过程中可以自定义的所有参数；
# 返回参数corners：检测到的aruco标记的角点列表，对于每个标记，其四个角点均按其原始顺序返回（从右上角开始顺时针旋转），第一个角是右上角，然后是右下角，左下角和左上角。
# 返回ids：检测到的每个标记的 id，需要注意的是第三个参数和第四个参数具有相同的大小；
# 返回参数rejectedImgPoints：抛弃的候选标记列表，即检测到的、但未提供有效编码的正方形。每个候选标记也由其四个角定义，其格式与第三个参数相同，该参数若无特殊要求可以省略。
