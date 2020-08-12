#히스토그램 inrange방법
# 범위를 주어 그 범위에 해당하는 부분만 추출한다.

# 실행 방법
#1. 추출하고 싶은 색 부분을 마우스로 드래그 한다.
#2. enter key를 누른다.

import sys
import numpy as np
import cv2


# 입력 영상에서 ROI를 지정하고, 히스토그램 계산

src = cv2.imread('.\chroma-key synthesis.\cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()


#ROI selector이다 즉 마우스를 이용하여 영역을 드래그하여 사용할 수 있다.
x, y, w, h = cv2.selectROI(src) 


#히스토그램을 계산하는 코드 ----
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w]

channels = [1, 2] #0번은 gray 값이므로 사용하지 않는다. => 밝기 정보이기 때문
cr_bins = 128 
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

#히스토그램 계산
hist = cv2.calcHist([crop], channels, None, histSize, ranges)
#-----------


hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대해 히스토그램 역투영


backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1) # 내가 원하는 부분만 골라내는 곳
dst = cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
