import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

h, w = img.shape[:2]
M = cv2.getPerspectiveTransform(np.float32([[0,0],[w-1,0],[0,h-1],[w-1,h-1]]),
                                np.float32([[50,50],[w-50,0],[0,h-50],[w-50,h-50]]))

out = cv2.warpPerspective(img, M, (w, h))

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-14_perspective_output.jpg", out)

cv2.imshow("Perspective", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
