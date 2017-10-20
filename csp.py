import numpy as np
import cv2

HEIGHT = 70
WIDTH = 1252  # 魔法の数字
pts1 = np.float32([[42, 0], [0, HEIGHT], [1210, 0], [WIDTH, HEIGHT]])
pts2 = np.float32([[0, 0], [0, HEIGHT], [WIDTH, 0], [WIDTH, HEIGHT]])
M = cv2.getPerspectiveTransform(pts1, pts2)

cap = cv2.VideoCapture('video.mp4')  # FullHD 60fps
cnt = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    cut = frame[880:950, 334:1586]  # 魔法の数字2

    print(cnt)

    pers = cv2.warpPerspective(cut, M, (WIDTH, HEIGHT))
    cv2.imshow('frame', pers)
    cv2.imwrite('png/%05d.png' % cnt, pers)
    cnt += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
