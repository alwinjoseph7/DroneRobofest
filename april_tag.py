import apriltag
import cv2
img = cv2.imread('apriltag2.png',cv2.IMREAD_GRAYSCALE)
result = apriltag.Detector().detect(img)
print(result[0][1])
