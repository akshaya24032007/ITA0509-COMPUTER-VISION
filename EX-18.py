import cv2

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\cv-1.png")

roi = img[10:60, 10:60]
img[70:120, 70:120] = roi

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-18_roi_output.jpg", img)

cv2.imshow("ROI Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
