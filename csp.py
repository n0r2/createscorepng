import numpy as np
import cv2
import sys


HEIGHT = 70
WIDTH = 1252  # 魔法の数字
pts1 = np.float32([[42, 0], [0, HEIGHT], [1210, 0], [WIDTH, HEIGHT]])
pts2 = np.float32([[0, 0], [0, HEIGHT], [WIDTH, 0], [WIDTH, HEIGHT]])
M = cv2.getPerspectiveTransform(pts1, pts2)

cap = cv2.VideoCapture(sys.argv[1])  # FullHD 60fps
cnt = 0
out = np.zeros((700, 125, 3), np.uint8)

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    cut = frame[880:950, 334:1586]  # 魔法の数字2

    print(cnt)

    pers = cv2.warpPerspective(cut, M, (WIDTH, HEIGHT))
    cv2.imshow('trimm', cut)
    cv2.imshow('pers', pers)
    resize_pers = cv2.resize(pers, (125, 7))
    out[(99 - (cnt % 100)) * 7:(99 - (cnt % 100)) * 7 + 7, :] = resize_pers
    cv2.imshow('out', out)
    cv2.imwrite('png/%05d.png' % cnt, pers)
    cnt += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
