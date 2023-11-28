import cv2
import numpy as np

img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

thresh_np = np.zeros_like(img)
thresh_np[img > 127] = 255
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("gray", img)
cv2.imshow("thresh", thresh_np)
cv2.imshow("thresh cv", thresh_cv)

cv2.waitKey()
cv2.destroyAllWindows()

blk_size = 9; C = 5
img = cv2.imread("./img/sudoku.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('paper', img)
_, t_80 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
otsu_thrshehole, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                            cv2.THRESH_BINARY, blk_size,C)

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                            cv2.THRESH_BINARY, blk_size,C)

cv2.imshow('totsu', t_otsu)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.waitKey()
cv2.destroyAllWindows()
print(otsu_thrshehole)
