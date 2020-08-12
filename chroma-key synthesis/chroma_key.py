# 크로마키 합성 
# - 녹색 또는 파란색 배경에서 촬영한 영상에 다른 배경 영상을 합성하는 기술

# 순서
# 1. 크로마키 영상을 HSV 색 공간으로 변환
# 2. cv2.inRange()를 사용하여 20<= H <= 80, 150 <= S <= 255, 0 <= V <= 255범위의 영역(녹색 부분)추출
# 3. cv2.copyTo()를 사용하여 녹색영역에 다른 배경 영상을 합성

import sys
import numpy as np
import cv2


# 녹색 배경 동영상
cap1 = cv2.VideoCapture('.\chroma-key synthesis.\woman.mp4')

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비오는 배경 동영상
cap2 = cv2.VideoCapture('.\chroma-key synthesis.\\raining.mp4')

if not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print('w x h: {} x {}'.format(w, h))
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) #시간 간격 


#출력 동영상 객체 생성 
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('croma_key_result.avi', fourcc, fps, (w, h))

# 합성 여부 플래그
# True면 합성 False면 합성하지 않는다.
do_composit = False


# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read() #동영상1

    if not ret1:
        break
    
    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        ret2, frame2 = cap2.read() #동영상2

        if not ret2:
            break

        # frame2 = cv2.resize(frame2,(w,h)) #번외 내 뒤에 녹색 배경일 때 / 크기 맞추기 
         
        
        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) #HSV로 변환
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255)) #번외 일때는 녹색의 범위를 맞춰줘야 한다.
        cv2.copyTo(frame2, mask, frame1) #frame2에서 mask가 흰 부분만 frame1으로 복사해라

    out.write(frame1) #출력 영상 저장 

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 do_composit 플래그를 변경
    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
