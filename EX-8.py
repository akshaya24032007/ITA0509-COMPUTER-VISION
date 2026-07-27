import cv2
import numpy as np

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

if img is None:
    print("Image not found!")
else:
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)

    cv2.imwrite("EX-8_Dilated_Image.png", dilated)

    cv2.imshow("Original", img)
    cv2.imshow("Dilated", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Output saved as EX-8_Dilated_Image.png")
