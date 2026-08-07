import cv2

img = cv2.imread(r"C:\Users\aksha\Downloads\ITA0509\Experiments\Watch.png")

cv2.putText(img, "WATCH", (40,40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

cv2.imwrite(r"C:\Users\aksha\Downloads\ITA0509\Experiments\EX-25_watch_output.jpg", img)

cv2.imshow("Watch", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
