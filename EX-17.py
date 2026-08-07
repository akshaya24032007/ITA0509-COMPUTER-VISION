import cv2

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

cv2.putText(img, "WATERMARK", (50,50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-17_watermark_output.jpg", img)

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
