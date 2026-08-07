import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\Dog.png", 0)

kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-21_opening_output.jpg", opening)

cv2.imshow("Opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
