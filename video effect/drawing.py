import numpy as np
import cv2
#(왼쪽부터 떨어진 거리, 위쪽부터 떨어진 거리)

img = np.full((400, 400, 3), 255, np.uint8)

#선 그리기(img, 시작점, 끝점, 색, 두께)
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

#사각형 그리기(img, 좌측상단꼭지점+(width, height), 색깔, 두께)
#사각형 그리기(img, 좌측상단꼭지점, 우측상단꼭지점, 색깔, 두께)
#thickness(두께)에서 음수 지정하면 내부를 채워준다.
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

#원그리기(img, 원의중심, 반지름, 색, 두께, line type)
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_8) #거친형태
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA) #부드러운 형태

pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]]) #numpy.ndarray의 리스트
#다각형 그리기(img, 다각형 외곽 점들의 좌표배열, 폐곡선 여부, 색, 두께, line type)
cv2.polylines(img, [pts], True, (255, 0, 255), 2)

#문자열 출력(img, 문자열, 출력하단좌표, 폰트, 크기, 색, 두께, line type)
text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

