import numpy as np
import cv2


# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8) #가로 240, 세로 320 => grayscale image, 모든 pixel은 grabage 값으로 채워진다.
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image, 모든 pixel은 0로 채워진다.
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray, 모든 pixel은 1로 채워진다.
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow, (0, 255, 255)해당 값으로 초기화 된다.

# 영상 보여주기 
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()



# 영상 복사
img1 = cv2.imread('.\\video effect.\HappyFish.jpg')

img2 = img1
img3 = img1.copy()

#img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('.\\video effect.\HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱(부분 가져오기)
img3 = img1[40:120, 30:150].copy()

img2.fill(0)
#img1[:,:] = (0,255,255)

#원 그려넣기 
cv2.circle(img2, (50,50), 20, (0,0,255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()
