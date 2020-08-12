# 특정 색상 영역 추출 
# RGB는 영상의 밝기에 따라서 잘 추출되지 않는다. 
# 그러나 hsv는 밝기에 상관 없이 잘 추출된다.
import sys
import numpy as np
import cv2


src = cv2.imread('.\chroma-key synthesis.\candies.png')
#src = cv2.imread('.\chroma-key synthesis.\candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) #hsv 로 변환

#inRange(src, lowerb, upperb, dst=None)
# lowerb(하한 값) ~ upperb(상한 값) 사이 값만 골라서 dst형태로 return 해준다.
dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100)) #(h,s,v) 값
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
