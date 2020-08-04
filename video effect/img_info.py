import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('.\\video effect.\cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('.\\video effect.\cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.shape:', img1.shape) #(세로,가로)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)
print('img2.dtype:', img2.dtype)


# 영상의 크기 참조
h, w = img2.shape[:2]
print('img2 size(w x h): {} x {}'.format(w, h))


# gray scale 확인하기 
if len(img1.shape) == 2: #img1.ndim도 2 출력
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()


# 영상의 픽셀 값 참조
# p1 = img1[y,x] => img1의 (x,y) 좌표에 있는 값
# p2 = img2[y,x] => img2의 (x,y) 좌표에 있는 값([블루, 그린, 레드])

#영상의 픽셀 값을 setting하는 것(오래걸리므로 하지 말것)
# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 255 #검정으로 setting
#         img2[y, x] = (0, 0, 255) #빨강색으로 setting  

img1[:,:] = 255 #검정으로 setting
img2[:,:] = (0, 0, 255) #빨강색으로 setting

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
