import cv2
img_file = "./img/test.jpg"
img = cv2.imread(img_file)
cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows()