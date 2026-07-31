import cv2

# Input image path
input_path = r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png"

# Output image path
output_path = r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\EX-11_output_180_rotation.jpg"

# Read image
image = cv2.imread(input_path)

# Check if image exists
if image is None:
    print("Error: Image not found!")
else:
    # Rotate 180 degrees
    rotated = cv2.rotate(image, cv2.ROTATE_180)

    # Save output automatically
    cv2.imwrite(output_path, rotated)

    print("Image rotated successfully.")
    print("Output saved at:")
    print(output_path)
