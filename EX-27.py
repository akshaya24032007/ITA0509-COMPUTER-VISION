import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\Face.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for (x, y, w, h) in face.detectMultiScale(gray, 1.3, 5):
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-27_face_output.jpg", img)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
