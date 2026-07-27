import cv2

# Read input video
cap = cv2.VideoCapture(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\Video.mp4")

# Get video size
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Save output video
out = cv2.VideoWriter("EX-7_output.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      30, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow("Video", frame)

    # 60 = Slow motion, 10 = Fast motion
    if cv2.waitKey(60) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Output saved as EX-7_output.mp4")
