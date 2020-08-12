# 자동으로 명암비 조절 
# 히스토그램 스트레칭 
# 히스토그램을 양쪽으로 늘려서 영상의 pixel값이 0 ~ 255까지 골고루 나타나게 해주는 것
# => 중간 중간 히스토그램에 빈 부분이 있다. 

import sys
import numpy as np
import cv2

#히스토그램 만들어 주는 함수 
def getGrayHistImage(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8) #가로 100 세로 256인 흰색 그림을 만든다.

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax)) #코드가 max값을 넘어가지 않게 하는 곳
        cv2.line(imgHist, pt1, pt2, 0) #밑에서 위로 선을 그어주고 있다.

    return imgHist 


src = cv2.imread('.\chroma-key synthesis.\Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


# nomalize() - 히스토그램 스트레칭하게 해준다.
#NORM_MINMAX - min, max값을 내가 원하는 값으로 한정시켜준다.
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX) 


#직선의 방정식을 계산해서 명암비를 주는 것이다.
# 방법 1 
# gmin, gmax, _, _ = cv2.minMaxLoc(src)
# dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)

# 방법 2 (numpy 사용)
# gmin = np.min(src)
# gmax = np.max(src)
# dst = np.clip((src - gmin) * 255. / (gmax - gmin), 0, 255).astype(np.uint8)

#히스토그램 출력 
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg2 = getGrayHistImage(hist2)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('src_hist', histImg)
cv2.imshow('dst_hist', histImg2)
cv2.waitKey()

cv2.destroyAllWindows()
