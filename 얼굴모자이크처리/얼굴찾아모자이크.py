# pip install opencv-python --> 이미지및 영상처리를 하기 위한 라이브러리 버전 4.6

import numpy as np  #
import cv2  # 이미지 및 영상처리를 하기위한 라이브러리

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


ff = np.fromfile(r"샘플이미지.jpg", np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 10)

for (x, y, w, h) in faces:
    face_img = img[y : y + h, x : x + w]
    # 찾아낸 얼굴 이미지 크기만큼만 가지고옴
    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.15, fy=0.15)
    # 가져온 이미지를 기존 사이즈에 0.15 배만큼 크기를 줄임
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
    # 다시 원래 사리즈로 늘림
    img[y : y + h, x : x + w] = face_img
    # 해당 이미지 위치로 다시가서 변경된 이미지 치환
cv2.imshow("face find", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
