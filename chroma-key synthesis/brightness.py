# src: 입력 값 
# dst: 출력 값
 
import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread('.\chroma-key synthesis.\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 픽셀값을 각각 100씩 더해서 밝게 해준다.
dst = cv2.add(src, 100) # == cv2.add(src, (100,0,0,0))
# dst = src + 100 => 이상하다(255보다 커질 시 <큰 수 - 255>로 저장된다. )
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('.\chroma-key synthesis.\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0)) #gray_scale 같이 100만 써주면 blue에만 100이 더해진다.
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
