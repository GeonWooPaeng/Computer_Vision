import sys 
import cv2

print("Hello, OpenCV", cv2.__version__)

#img 라는 영상 파일 불러오기(cat.bmp가 현재 파일에 존재해야한다.)
img = cv2.imread('.\image slide show\cat.bmp')

#예외처리(cat.bmp)에 대한
if img is None:
    print("Image load failed")
    sys.exit() 

cv2.namedWindow('image') #image란 이름의 새 창을 생성 
cv2.imshow('image',img) #image창에다가 img의 영상을 보여준다.
cv2.waitKey() #키보드 입력이 있을 때까지 대기

cv2.destroyAllWindows() #생성된 모든 창을 닫는다.