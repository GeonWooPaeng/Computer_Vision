import sys
import cv2



cap = cv2.VideoCapture(0) #카메라 open하기

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FPS
# => 초당 frame 수 (현재 frame에서 다음 frame과의 시간 간격)
fps = cap.get(cv2.CAP_PROP_FPS)


# fourcc(four character code)
# => 어떤 압축 방식을 사용할 것인가 
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X' => 둘 중 1개 쓰면 된다.
delay = round(1000 / fps)

#video를 만드는 곳
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame #frame을 반전

    # gray_scale이라 저장이 안된다. 그래서 color로 바꿔줘야 한다.
    edge = cv2.Canny(frame, 50, 150)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) #gray => color로 바꿔주기

    #영상 데이터만 저장한다(소리 X)
    out.write(inversed) 
    # out.write(edge)

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
