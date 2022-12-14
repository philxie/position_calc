#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 找棋盘格角点标定并且写入文件

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)  # 阈值

# 棋盘格模板规格
w = 7  # 8 - 1
h = 5  # 6  - 1

# 世界坐标系中的棋盘格点,例如(0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)，去掉Z坐标，记为二维矩阵
objp = np.zeros((w * h, 3), np.float32)
objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)

# 估计是各自边长，很多代码没有这个
objp = objp * 94.5  # 18.1 mm

# 储存棋盘格角点的世界坐标和图像坐标对
objpoints = []  # 在世界坐标系中的三维点
imgpoints = []  # 在图像平面的二维点

images = glob.glob('./*.jpg')  # 拍摄的十几张棋盘图片所在目录

i = 1
for fname in images:

    img = cv2.imread(fname)
    # 获取画面中心点

    h1, w1 = img.shape[0], img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    u, v = img.shape[:2]
    # 找到棋盘格角点
    ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
    # 如果找到足够点对，将其存储起来
    if ret == True:
        print("i:", i)
        i = i + 1

        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners)
        # 将角点在图像上显示
        cv2.drawChessboardCorners(img, (w, h), corners, ret)
        cv2.namedWindow('findCorners', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('findCorners', 640, 480)
        cv2.imshow('findCorners', img)
        cv2.waitKey(200)
cv2.destroyAllWindows()
# %% 标定
print('正在计算')
ret, mtx, dist, rvecs, tvecs = \
    cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
cv_file = cv2.FileStorage("camera.yaml", cv2.FILE_STORAGE_WRITE)
cv_file.write("camera_matrix", mtx)
cv_file.write("dist_coeff", dist)
# 请注意，*释放*不会关闭（）FileStorage对象

cv_file.release()

print("ret:", ret)
print("mtx:\n", mtx)  # 内参数矩阵
print("dist畸变值:\n", dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
print("rvecs旋转（向量）外参:\n", rvecs)  # 旋转向量  # 外参数
print("tvecs平移（向量）外参:\n", tvecs)  # 平移向量  # 外参数
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (u, v), 0, (u, v))
print('newcameramtx外参', newcameramtx)

url = 'rtsp://admin:admin@10.12.97.126:8554/live'
camera = cv2.VideoCapture(url)

# dist=np.array(([[-0.3918239532375715, 0.1553689004591761, 0.001069066277469635, 2.175204930902934e-06, -0.02850420360197434]]))
# # newcameramtx=np.array([[1.85389837e+04 ,0.00000000e+00, 5.48743017e+02]
# #  ,[  0 ,2.01627296e+04 ,4.52759577e+02]
# #  ,[0, 0, 1]])
# mtx=np.array([[379.1368428730273, 0, 312.1210537268028],
#  [  0, 381.6396537294123, 242.492484246843],
#  [  0.,           0.,           1.        ]])


while True:
    (grabbed, frame) = camera.read()
    h1, w1 = frame.shape[:2]
    # 打开标定文件
    cv_file = cv2.FileStorage("camera.yaml", cv2.FILE_STORAGE_READ)
    camera_matrix = cv_file.getNode("camera_matrix").mat()
    dist_matrix = cv_file.getNode("dist_coeff").mat()
    cv_file.release()

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_matrix, (u, v), 0, (u, v))
    # 纠正畸变
    dst1 = cv2.undistort(frame, camera_matrix, dist_matrix, None, newcameramtx)
    # dst2 = cv2.undistort(frame, mtx, dist, None, newcameramtx)
    mapx, mapy = cv2.initUndistortRectifyMap(camera_matrix, dist_matrix, None, newcameramtx, (w1, h1), 5)
    dst2 = cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)

    # 裁剪图像，输出纠正畸变以后的图片
    x, y, w1, h1 = roi
    dst1 = dst1[y:y + h1, x:x + w1]

    cv2.imshow('dst1', dst1)
    # cv2.imshow('dst2', dst2)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q保存一张图片
        cv2.imwrite("../u4/frame.jpg", dst1)
        break

camera.release()
cv2.destroyAllWindows()


# mtx -->内参数矩阵
# dist --> 畸变系数
# rvecs --> 旋转向量
# tvecs --> 平移向量