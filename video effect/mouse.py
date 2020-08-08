# 마우스 이벤트
#cv2.setMouseCallback(windowName, onMouse, param=None)
# windowName: 마우스 이벤트 처리를 수행할 창 이름
# onMouse: 마우스 이벤트 처리를 위한 콜백 함수(형식있다.)
# param: 콜백 함수에 전달할 데이터

#onMouse(event,x,y,flags,param)
# event: 마우스 이벤트의 종류(마우스로 만)
# x,y: 마우스 이벤트 발생 좌표
# flags: 마우스 이벤트가 발생할 때 키보드 또는 마우스 상태(ctrl+마우스 등등) => 각 bit가 세팅되어 있는지 확인

import sys
import numpy as np
import cv2


oldx = oldy = -1

def on_mouse(event, x, y, flags, param): #인자를 다 안쓰더라도 써줘야 한다.
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        #마우스를 움직이면 계속 발생
        if flags == cv2.EVENT_FLAG_LBUTTON: #flags에서 다른 것이 눌러진 것을 판단하지 못한다.
            
            # 선 그리는 부분
            # cv2.circle(img, (x,y), 4, (0,0,255), -1) # 빨리 그릴시 끊어짐이 발생한다.
            
            #이전부터 현재까지 이어지는 선 형태로 만들어야 빨리 그려도 끊어짐이 없다.
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA) 
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')

#위치 중요(namedWindow(), imshow()가 호출된 이후에 써야된다.)
cv2.setMouseCallback('image', on_mouse, img) 

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
