import cv2
import numpy as np

#img = np.full((500,500,3), 255, dtype=np.uint8)
#cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
#cv2.putText(img,"아름다운 강산-김성찬",(50,208), \
#           cv2.FONT_HERSHEY_PLAIN,4,(0,0,0))
#cv2.imshow('draw text', img)
#cv2.waitKey()
#cv2.destroyAllWindows()

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = np.full(shape=(512,512,3),fill_value=255,dtype=np.uint8)
img = Image.fromarray(img) #img배열을 PIL이 처리가능하게 변환

draw = ImageDraw.Draw(img)
font=ImageFont.truetype("fonts/gulim.ttc",20)
org=(50,100)
text="아름다운 강산 - 김성찬"
draw.text(org,text,font=font,fill=(0,0,0)) #text를 출력
img = np.array(img) #다시 OpenCV가 처리가능하게 np 배열로 변환


cv2.imshow("A",img)
cv2.waitKey()
cv2.destroyAllWindows()