# 히스토그램
# 영상의 픽셀 값 분포를 그래프의 형태로 표현한 것 
# ex) 그레이스케일 영상에서 각 그레이스케일 값에 해당하는 픽셀의 개수를 구하고, 이를 막대 그래프의 형태로 표현 

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


# 그레이스케일 영상의 히스토그램
src = cv2.imread('.\chroma-key synthesis.\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.calcHist(img, channels, mask, histSize, ranges, hist=None, accumulate=None)
# channels: [0]이면 gray_scale, [0,1]이면 blue + green, [0,1,2]이면 blue + gree + red 
# mask: None이면 입력 영상 전체에서 히스토그램을 구함
# histSize: [256]은 0부터 25까지 받겠다. 히스토그램 각 차원의 크기(빈(bin)의 개수)를 나타내는 리스트
# ranges: 히스토그램 각 차원의 최솟값과 최댓값 
# hist: 계산된 히스토그램
# accumulate: 누적이면 True, 새로 만들면 False

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist) #1차원 그래프를 편하게 보여준다.
plt.show()

# 컬러 영상의 히스토그램
src = cv2.imread('.\chroma-key synthesis.\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()
