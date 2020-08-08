import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture() #cv2.VideoCapture(0)이면 cap.open()을 안써도 된다.
cap.open(0) # 기본카메라를 open하겠다.

#카메라 켜졌는지 확인
if not cap.isOpened(): 
    print('camera open failed!')
    sys.exit() 

while True:
    #현재 open되어 있는 camera에서 1 frame씩 받아온다.출력 => (bool, array)
    ret, frame = cap.read() 

    if not ret:
        break 
    
    #inversed = ~frame #반전  
    edge = cv2.Canny(frame, 50, 150)#윤각선을 보여주는 것

    cv2.imshow('frame', frame)# 동영상 보요주기
    cv2.imshow('edge', edge) #윤각선 동영상 보여주기 

    if cv2.waitKey(20) == 27: #ESC 눌렀을떄 
        break 

cap.release() #cap을 해제한다.
cv2.destroyAllWindows() #모든 창을 닫는다.


#카메라 속성을 알기 위한 함수 
# cap.get(cv2.CAP_PROP_FRAME_WIDTH) 

#카메라 속성을 받아오기 위한 함수(320을 넓이로 받아오기)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)