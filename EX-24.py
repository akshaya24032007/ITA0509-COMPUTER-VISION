import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\cv-1.png", 0)

kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-24_blackhat_output.jpg", blackhat)

cv2.imshow("Black Hat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
