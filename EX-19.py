import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\cv-1.png", 0)

kernel = np.ones((5,5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-19_eroded_output.jpg", eroded)

cv2.imshow("Eroded Image", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
