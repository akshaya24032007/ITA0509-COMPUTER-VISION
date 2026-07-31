import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")
gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-15_harris_output.jpg", img)

cv2.imshow("Harris Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
