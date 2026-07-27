import cv2

# Give the correct image path
img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

# Check if image is loaded
if img is None:
    print("Image not found! Check the file name and path.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-3_canny_output.jpg", edges)

    cv2.imshow("Original", img)
    cv2.imshow("Canny Output", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
