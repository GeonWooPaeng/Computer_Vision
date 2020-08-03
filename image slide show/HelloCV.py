import sys 
import cv2

print("Hello, OpenCV", cv2.__version__)

#img 라는 영상을 만든다 
img = cv2.imread('cat.bmp')

#예외처리(cat.bmp)에 대한
if img in None:
    print("Image load failed")
    sys.exit() 

cv2.namedWindow('imgae') #창을 생성 
cv2.imshow('image',img) #imgae창에다가 img의 영상을 보여준다.
cv2.waitKey() #화면에 실제로 보여지게 한다.

cv2.destroyAllWindows() #기존에 나타나 있는화면을 닫아라 