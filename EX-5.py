import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\cv-1.png")

for i, c in enumerate(('b', 'g', 'r')):
    plt.plot(cv2.calcHist([img], [i], None, [256], [0, 256]), color=c)

plt.savefig(r"C:\Users\aksha\OneDrive\Desktop\New folder\IT0509-COMPUTER VISION\histogram_output.png")
plt.show()
