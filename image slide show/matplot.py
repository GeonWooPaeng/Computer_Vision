import matplotlib.pyplot as plt 
import cv2  

# 컬러 영상 출력 
imgBGR = cv2.imread('.\image slide show\cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) #BGR을 RGB로 바꾸는 것

plt.axis('off') # 가로 세로 눈금 없애는 방법
plt.imshow(imgRGB)
plt.show() 

# 그레이스케일 영상 출력 
imgGray = cv2.imread('.\image slide show\cat.bmp', cv2.IMREAD_GRAYSCALE) #2차원 형태로 밝기 값만 저장

plt.axis('off') # 가로 세로 눈금 없애는 방법
plt.imshow(imgGray, cmap='gray')
plt.show() 

# 두개의 영상을 함께 출력
# subplot(121) - 1개의 행에 표현하고 2개의 열로 나누고 1번째 열에 넣어라(1,2-1) 
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show() 