import math

import cv2
import numpy as np


import cv2
import numpy as np

img_file = "./img/girl.jpg"  # 표시할 이미지 경로            ---①
img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②
print(img.shape)

cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시      --- ③
cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤

imgy = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
y, u, c = cv2.split(imgy)
cv2.imshow("YUV", y)
cv2.waitKey()
cv2.destroyAllWindows()

# Y = 0.299R + 0.587G + 0.114B



b, g, r = cv2.split(img)
cy = np.full_like(b, 255, dtype = np.uint8)
cy = b*0.114 + g*0.587 + r*0.299