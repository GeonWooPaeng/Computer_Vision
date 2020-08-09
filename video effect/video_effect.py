# 동영상 전환 effect 
# 두 동영상 클립 사이에 추가되는 애니메이션 효과

# 구현 기능 
# 두 개의 동영상 동시 열기 
# 첫 번째 동영상의 마지막 n개 프레임과 두 번째 동영상의 처음 n개 프레임을 합성 
# 합성된 영상을 동영상으로 저장하기 

import sys
import numpy as np
import cv2


# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('.\\video effect.\\video1.mp4')
cap2 = cv2.VideoCapture('.\\video effect.\\video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2) #2초가 합쳐져서 동작하게 한다.

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

delay = int(1000 / fps) #두 frame사이의 시간 간격 표시

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

#첫번째 동영상
for i in range(frame_cnt1 - effect_frames): #뒤의 48frame 정도 남겨둔다.
    ret1, frame1 = cap1.read() 

    if not ret1:
        break 

    out.write(frame1)

    cv2.imshow('frame1', frame1)
    cv2.waitKey(delay)

#합성하는 구간
for i in range(effect_frames): 
    ret1, frame1 = cap1.read() 
    ret2, frame2 = cap2.read() 

    # 합성
    dx = int(w * i / effect_frames) #잘라낼 위치

    #주의!!
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    #frame[:, 0:dx] = frame2[:, 0:dx]
    #frame[:, dx:w] = frame1[:, dx:w]
    
    #바뀔 때 첫 영상 흐려지면서 다음 영상 출력
    alpha = 1.0 - i / effect_frames  #0~1사이 값
    frame = cv2.addWeighted(frame1, alpha, frame2, 1 - alpha, 0)
    
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)

#두번째 동영상 출력
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read() 

    if not ret2:
        break 

    out.write(frame2)

    cv2.imshow('frame2', frame2)
    cv2.waitKey(delay)


cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()


# <합성 부분 정리 코드>

# # 1번 동영상 복사
# for i in range(frame_cnt1 - effect_frames):
#     ret1, frame1 = cap1.read()

#     if not ret1:
#         print('frame read error!')
#         sys.exit()

#     out.write(frame1)
#     print('.', end='')

#     cv2.imshow('output', frame1)
#     cv2.waitKey(delay)

# # 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
# for i in range(effect_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     if not ret1 or not ret2:
#         print('frame read error!')
#         sys.exit()

#     dx = int(w / effect_frames) * i

#     frame = np.zeros((h, w, 3), dtype=np.uint8)
#     frame[:, 0:dx, :] = frame2[:, 0:dx, :]
#     frame[:, dx:w, :] = frame1[:, dx:w, :]

#     #alpha = i / effect_frames
#     #frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

#     out.write(frame)
#     print('.', end='')

#     cv2.imshow('output', frame)
#     cv2.waitKey(delay)

# # 2번 동영상을 복사
# for i in range(effect_frames, frame_cnt2):
#     ret2, frame2 = cap2.read()

#     if not ret2:
#         print('frame read error!')
#         sys.exit()

#     out.write(frame2)
#     print('.', end='')

#     cv2.imshow('output', frame2)
#     cv2.waitKey(delay)

# print('\noutput.avi file is successfully generated!')