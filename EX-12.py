import cv2

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-12_rotation270_output.jpg", rotated)

cv2.imshow("270 Degree Rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
