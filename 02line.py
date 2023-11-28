import cv2
import numpy as np
img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.line(img, (50,50), (150,50), (255,0,0))
cv2.line(img, (200,50), (300,50), (0,255,0))
cv2.line(img, (350,50), (450,50), (0,0,255))

cv2.line(img, (100,100), (400,100), (255,255,0), 10)
cv2.line(img, (100,150), (400,160), (255,0,255), 10)
cv2.line(img, (150,200), (450,200), (0,255,255), 20)

cv2.line(img, (100,350), (400,400), (0,0,0), 20, cv2.LINE_4)
cv2.line(img, (100,400), (400,450), (50,50,50), 20, cv2.LINE_8)
cv2.line(img, (150,450), (400,500), (100,100,100), 20, cv2.LINE_AA)


cv2.imshow("lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()