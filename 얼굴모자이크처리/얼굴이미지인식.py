# pip install opencv-python --> 이미지및 영상처리를 하기 위한 라이브러리

import numpy as np
import cv2  # 이미지 및 영상처리를 하기위한 라이브러리

face_cascade = cv2.CascadeClassifier(  # 케스케이드 분류기 음영의 특징을 구분하여 얼굴을 인식하는데 사용
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)  # 사전 훈련된 하르케스케이드를 불러와 적용시킴 얼굴의 이미지특장점을 6000개로 구분하여 얼굴인식
eye_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
# 동일하게 사전훈련된 하르케스케이드를 불러와 눈을 인식시킴

ff = np.fromfile(r"샘플이미지.jpg", np.uint8)  # np.uint8 ->한글파일을 인식시켜줌
print(type(ff))  # np.fromfile 이미지 파일을 다차원 배열 객체로 받아오는 함수
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# IMREAD_UNCHANGED파일 속성 그대로 읽어오기
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 명확한 구분을 위하여 컬러변환 함수 cvtColor를 사용하여 사진 img를 cv2.COLOR_BGR2GRAY
faces = face_cascade.detectMultiScale(gray, 1.2, 10)
# detectMultiScale 흑백으로전환된 사진에서 얼굴위치를 검출하여 튜플형태의 리스트로 리턴해줌 (x,y,w,h)
# x,y 는 좌상단 기준 얼굴 시작지점 좌표 w,h 는 가로 세로 의 길이를 리턴해줍니다.
# detectMultiScale(이미지,정밀도,얼굴사이 간격)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # 직사각형을 그려주는 도구 이미지에, x,y 좌표를 시작으로 x + w, y + h 만큼
    # 원하는 색상, 선굵기 를 정하여 그려줌
    roi_gray = gray[y : y + h, x : x + w]
    # 인식된 얼굴안에서 눈을 찾아내기 위해 흑백처리
    roi_color = img[y : y + h, x : x + w]
    eyes = eye_casecade.detectMultiScale(roi_gray)
    # 눈위치를 리턴받음
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        # 눈위치에 사각형 생성

cv2.imshow("face find", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
