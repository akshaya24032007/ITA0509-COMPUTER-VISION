import cv2

# Read image
img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

# Check image
if img is None:
    print("Image not found!")
else:
    # Resize
    bigger = cv2.resize(img, None, fx=2, fy=2)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Save output
    cv2.imwrite("EX-9_Bigger.png", bigger)
    cv2.imwrite("EX-9_Smaller.png", smaller)

    # Display
    cv2.imshow("Original", img)
    cv2.imshow("Bigger", bigger)
    cv2.imshow("Smaller", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Outputs saved successfully.")
