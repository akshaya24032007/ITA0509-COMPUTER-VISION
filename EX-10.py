import cv2

# Read input image
img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

# Rotate 90° clockwise
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Save output automatically
cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-10_Rotated.jpg", rot)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Rotated", rot)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Output saved as EX-10_Rotated.jpg")
