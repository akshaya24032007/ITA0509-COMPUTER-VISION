import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\Dog.png", 0)

kernel = np.ones((5,5), np.uint8)
dilated = cv2.dilate(img, kernel, iterations=1)

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-20_dilated_output.jpg", dilated)

cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
