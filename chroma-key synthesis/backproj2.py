# 히스토그램 역투영
# 임의의 색상 영역을 검출할때 효과적 
# ycrcb를 주로 사용 

# 히스토그램 역투영을 이용하여 살색을 검출 => 범위가 아니라 내가 원하는 부분대로 작성 가능하다
# mask를 이용하여 추출하고 싶은 부분(흰색부분)을 추출하고 그것을 가지고 다른 영상에 사용하는 방법

# 1. 기준 영상에서 살색에 대한 컬러 히스토그램을 미리 계산
# 2. 입력 영상에서 미리 구한 살색 히스토그램에 부합하는 픽셀을 선별 

import sys
import numpy as np
import cv2


# CrCb 살색 히스토그램 구하기
ref = cv2.imread('.\chroma-key synthesis.\kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('.\chroma-key synthesis.\kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]

# 히스토그램을 가져다가 출력을 해주는 것, 특정 mask영역에서 히스토그램을 구하고 싶다.(2차원 형태)
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)

# hist를 화면으로 보고 싶어 gray_scale영상으로 변환 / log로 해주는 것이 좋다.
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, 
                          cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('.\chroma-key synthesis.\kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

#calcHist에서 계산된 값을 입력으로 받아 확률과 같은 img로 반환해준다./ gray_scale형태이므로 그냥 imshow해도 된다.
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1) 

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj) 
cv2.waitKey()
cv2.destroyAllWindows()
