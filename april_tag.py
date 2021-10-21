import apriltag
import cv2
img = cv2.imread('apriltag2.png',cv2.IMREAD_GRAYSCALE)
detector = apriltag.Detector()
result = detector.detect(img)
print(result[0][1])
