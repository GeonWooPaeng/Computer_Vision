import sys
import cv2

# 마스크 영상을 이용한 영상 합성
src = cv2.imread('.\\video effect.\\airplane.bmp', cv2.IMREAD_COLOR) #src 영상
mask = cv2.imread('.\\video effect.\\mask_plane.bmp', cv2.IMREAD_GRAYSCALE) #dst 영상
dst = cv2.imread('.\\video effect.\\field.bmp', cv2.IMREAD_COLOR) #mask 영상 => 포토샵등을 이용해서 만든 것이다.

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.copyTo(src, mask) #검정색 배경에 src를 넣는다. => 그래서 dst를 입력(안에다)을 줘야한다.
cv2.copyTo(src, mask, dst) #src영상을 mask를 이용해서 dst에 적용하는 것이다.(dst를 입력으로 준 것)
# < src, mask, dst는 size가 다 같아야 한다, src와 dst는 type이 같아야 한다., mask는 무조건 GRAYSCALE Type>

# dst[mask > 0] = src[mask > 0] #boolien indexing

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()


# 알파 채널을 마스크 영상으로 이용
# 정보를 알고 싶은 곳 번호(붉은 색)누른 후 디버깅하고 그 곳을 가리켜 보면 정보를 볼 수 있다.
src = cv2.imread('.\\video effect.\cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('.\\video effect.\opencv-logo-white.png', cv2.IMREAD_UNCHANGED) #channel이 4개자리를 가져오기 위해서 IMREAD_UNCHANGED를 사용한다.

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상(가로,세로 다가져오고 마지막 channel 1개 가져온다)
h, w = mask.shape[:2]

crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
