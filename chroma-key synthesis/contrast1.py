# 명암비
# 영상을 입력으로 주기전에 전처리 과정으로 많이 사용하는 방법이다.
# 밝은 곳과 어두운 곳 사이에 드러나는 밝기 정도의 차이
 
import sys
import numpy as np
import cv2


src = cv2.imread('.\chroma-key synthesis.\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8) #해당 값을  0 ~ 255사이이며 float이므로 uint8을 해준 것이다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
