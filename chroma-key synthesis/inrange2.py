# hsv - 원색을 찾을 때 좋다
# h: 각도로 색을 나타낸다 but 360도 전체로 하는 것이 아니라 180도를 전체 원으로 한다.(90 -> 45)
# s: 원 중심(0), 테두리가 255이다.
# v: 밝기
import sys
import numpy as np
import cv2


src = cv2.imread('.\chroma-key synthesis.\candies.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) #hsv로 변환

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst') #dst 창에 있는 H_min trackbar의 위치를 받아오는 함수 
    hmax = cv2.getTrackbarPos('H_max', 'dst')

    #inRange(src, lowerb, upperb, dst=None)
# lowerb(하한 값) ~ upperb(상한 값) 사이 값만 골라서 dst형태로 return 해준다.
    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)


cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar) #H값의 lowerb
cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar) #H값의 upperb
on_trackbar(0)

cv2.waitKey()

cv2.destroyAllWindows()
