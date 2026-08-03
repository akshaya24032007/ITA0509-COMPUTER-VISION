import cv2

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-1_grayscale_output.jpg", gray)
    cv2.imshow("Original", img)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
