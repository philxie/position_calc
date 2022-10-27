import cv2

url = 'rtsp://admin:admin@10.12.97.126:8554/live'
camera = cv2.VideoCapture(url)
i = 0
while 1:
    (grabbed, img) = camera.read()
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('j'):  # 按j保存一张图片
        i += 1
        u = str(i)
        firename = str('./img' + u + '.jpg')
        cv2.imwrite(firename, img)
        print('写入：', firename)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
