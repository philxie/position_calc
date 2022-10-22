* 展开所支持的标记字典

展开查看的内容;
DICT_4X4_50 
Python: cv.aruco.DICT_4X4_50
DICT_4X4_100 
Python: cv.aruco.DICT_4X4_100
DICT_4X4_250 
Python: cv.aruco.DICT_4X4_250
DICT_4X4_1000 
Python: cv.aruco.DICT_4X4_1000
DICT_5X5_50 
Python: cv.aruco.DICT_5X5_50
DICT_5X5_100 
Python: cv.aruco.DICT_5X5_100
DICT_5X5_250 
Python: cv.aruco.DICT_5X5_250
DICT_5X5_1000 
Python: cv.aruco.DICT_5X5_1000
DICT_6X6_50 
Python: cv.aruco.DICT_6X6_50
DICT_6X6_100 
Python: cv.aruco.DICT_6X6_100
DICT_6X6_250 
Python: cv.aruco.DICT_6X6_250
DICT_6X6_1000 
Python: cv.aruco.DICT_6X6_1000
DICT_7X7_50 
Python: cv.aruco.DICT_7X7_50
DICT_7X7_100 
Python: cv.aruco.DICT_7X7_100
DICT_7X7_250 
Python: cv.aruco.DICT_7X7_250
DICT_7X7_1000 
Python: cv.aruco.DICT_7X7_1000
DICT_ARUCO_ORIGINAL 
Python: cv.aruco.DICT_ARUCO_ORIGINAL
DICT_APRILTAG_16h5 
Python: cv.aruco.DICT_APRILTAG_16h5
4x4 bits, minimum hamming distance between any two codes = 5, 30 codes

>对于每次成功检测到标记，将按从左上，右上，右下和左下的顺序检测标记的四个角点。在C ++中，将这4个检测到的角点存储为点矢量，并将图像中的多个标记一起存储在点矢量容器中。在Python中，它们存储为Numpy 数组。
detectMarkers()函数用于检测和确定标记角点的位置。
第一个参数image是带有标记的场景图像。
第二个参数dictionary是用于生成标记的字典。成功检测到的标记将存储在markerCorners中，其ID存储在markerIds中。先前初始化的DetectorParameters对象作为传递参数。
第三个参数parameters： DetectionParameters 类的对象，该对象包括在检测过程中可以自定义的所有参数；
返回参数corners：检测到的aruco标记的角点列表，对于每个标记，其四个角点均按其原始顺序返回（从右上角开始顺时针旋转），第一个角是右上角，然后是右下角，左下角和左上角。
返回ids：检测到的每个标记的 id，需要注意的是第三个参数和第四个参数具有相同的大小；
返回参数rejectedImgPoints：抛弃的候选标记列表，即检测到的、但未提供有效编码的正方形。每个候选标记也由其四个角定义，其格式与第三个参数相同，该参数若无特殊要求可以省略。
```python
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,aruco_dict,parameters=parameters)
```

>当我们检测到aruco标签之后,为了方便观察,我们需要进行可视化操作,把标签标记出来:使用drawDetectedMarkers（）这个API来绘制检测到的aruco标记，其参数含义如下：
参数image: 是将绘制标记的输入 / 输出图像（通常就是检测到标记的图像）
参数corners：检测到的aruco标记的角点列表
参数ids：检测到的每个标记对应到其所属字典中的id,可选（如果未提供）不会绘制ID。
参数borderColor：绘制标记外框的颜色,其余颜色（文本颜色和第一个角颜色）将基于该颜色进行计算，以提高可视化效果。
无返回值
```python
aruco.drawDetectedMarkers(image, corners,ids,borderColor)
```
