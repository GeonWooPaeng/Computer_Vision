import sys
import glob
import cv2

# 이미지 파일을 모두 img_files 리스트에 추가
img_files = glob.glob('.\image slide show\.\\images\\*.jpg')

# img_files 유/무 확인 하기
if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit() 

# 전체 화면 영상 출력하기 
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0 

while True:
    img = cv2.imread(img_files[idx%cnt])
    cv2.imshow('image', img)

    if cv2.waitKey(1000) >= 27: #ESC 
        break 

    idx+=1 

cv2.destroyAllWindows() 
