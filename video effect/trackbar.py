# trackbar: 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤 
import numpy as np
import cv2


def on_level_change(pos): #위치(pos)를 받는다. 
    global img

    value = pos * 16 

    #255가 최대 이므로 최대를 255로 고정시킨다.
    #level = np.clip(level, 0, 255) # 범위: 0~255
    if value >= 255:
        value = 255


    img[:] = value
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')

#창이 생성된 이후에 생성해야 된다.
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
