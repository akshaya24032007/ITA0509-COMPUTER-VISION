import cv2

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png", 0)

sx = cv2.convertScaleAbs(cv2.Sobel(img, cv2.CV_64F, 1, 0))
sy = cv2.convertScaleAbs(cv2.Sobel(img, cv2.CV_64F, 0, 1))
sc = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-16_Sobel_X.jpg", sx)
cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-16_Sobel_Y.jpg", sy)
cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-16_Sobel_Combination.jpg", sc)

cv2.imshow("Sobel_X", sx)
cv2.imshow("Sobel_Y", sy)
cv2.imshow("Sobel_Combination", sc)

cv2.waitKey(0)
cv2.destroyAllWindows()
