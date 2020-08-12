# 히스토그램 평활화 
# 색상정보랑 밝기 정보를 따로 처리해야 된다.
# 히스토그램이 그레이스케일 전체 구간에서 균일한 분포로 나타나도록 변경하는 명암비 향상 기법
# 균일 간격으로 히스토그램에 빈칸이 들어가지 않는다. => 뭉쳐있는 부분을 넓게 펴고 안 뭉쳐있는 부분은 넓게 피지 않는다.

import sys
import numpy as np
import cv2


# 그레이스케일 영상의 히스토그램 평활화
src = cv2.imread('.\chroma-key synthesis.\Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 컬러 영상에 히스토그램 평활화 적용
src = cv2.imread('.\chroma-key synthesis.\\field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb) #3개 짜리 리스트를 가진다.

# 밝기 성분(y, ycrcb_planes[0])에 대해서만 히스토그램 평활화 수행
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes) #다시 합친다.
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR) #YCrCb -> BGR로 변환

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
