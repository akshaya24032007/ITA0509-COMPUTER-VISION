import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

kernel = np.ones((5,5), np.uint8)
erode = cv2.erode(img, kernel, iterations=1)

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-6-erode_output.jpg", erode)

cv2.imshow("Original", img)
cv2.imshow("Eroded", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
