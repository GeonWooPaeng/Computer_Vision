#cv2.waitKeyEx() 키보드 특수키 사용

import sys
import numpy as np
import cv2

img = cv2.imread('.\\video effect.\cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    keycode = cv2.waitKey() 
    #변수로 받아줘야 key board입력을 한번으로 된다.
    # keycode를 해주는 대신 cv2.waitKey()로 대체하면 2번 눌러야 한다.
    
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img #반전
        cv2.imshow('image', img)
    elif keycode == 27:
        break

cv2.destroyAllWindows()
