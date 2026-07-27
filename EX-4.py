import cv2

# Read image in grayscale
img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png", 0)

# Histogram Equalization
eq = cv2.equalizeHist(img)

# Save output automatically
cv2.imwrite(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-4_Output.jpg", eq)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Equalized", eq)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Output saved as EX-4_Output.jpg")
