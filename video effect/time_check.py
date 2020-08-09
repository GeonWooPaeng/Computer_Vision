# 보통 30ms 이하로 되야지 괜찮은 것이다.
# 20번 정도 돌려서 시간 check해야 한다.

import sys
import time #파이썬 기능
import numpy as np
import cv2 #opencv 기능


img = cv2.imread('.\\video effect.\hongkong.jpg')

tm = cv2.TickMeter()

tm.reset() #시간 측정 초기화
tm.start() #시간 측정 시작
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

tm.stop() #시간 측정 끝
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli())) #strat 부터 stop까지의 시간

