import cv2

# Read image
img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (15, 15), 0)

# Save output in the same folder
cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-2_blur_output.jpg", blur)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
