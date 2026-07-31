import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

M = cv2.getAffineTransform(np.float32([[50,50],[200,50],[50,200]]),
                           np.float32([[10,100],[200,50],[100,250]]))

out = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-13_affine_output.jpg", out)

cv2.imshow("Affine", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
