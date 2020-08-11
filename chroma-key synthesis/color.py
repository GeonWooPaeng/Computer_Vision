# opencv & 컬러영상 
# 컬러영상은 3차원 numpy.ndarray로 표현. img.shape = (h,w,3)
# opencv에서는 BGR 순서를 기본으로 사용

#RGB 색상 -> Gray_Scale 
# Y = 0.299R + 0.587G + 0.114B 

import sys
import numpy as np
import cv2

# 컬러 영상 불러오기
src = cv2.imread('.\chroma-key synthesis.\candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)

#b_plane = src[:, :, 0]  
#g_plane = src[:, :, 1] 
#r_plane = src[:, :, 2] 

cv2.imshow('src', src)
cv2.imshow('B_plane', b_plane) # 파란색이 밝게 나타나는 부분
cv2.imshow('G_plane', g_plane) # 그린이 밝게 나타나는 부분
cv2.imshow('R_plane', r_plane) # 빨강이 밝게 나타나는 부분
cv2.waitKey()

cv2.destroyAllWindows()

#HSV 만들기 
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
plane = cv2.split(src_hsv)

cv2.imshow('src', src)
cv2.imshow('plane[0]', plane[0]) 
cv2.imshow('plane[1]', plane[1]) 
cv2.imshow('plane[2]', plane[2]) 
cv2.waitKey()

cv2.destroyAllWindows()