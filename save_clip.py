import cv2
import random

cap=cv2.VideoCapture(0)
filename=str(random.randint(0,1000))+".avi"
clip=cv2.VideoWriter(filename,cv2.VideoWriter_fourcc('M','J','P','G'),30,(int(cap.get(3)),int(cap.get(4))))

while True:
    _,frame=cap.read()
    cv2.imshow('video',frame)
    clip.write(frame)
    if cv2.waitKey(5) & 0xFF != ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
clip.release()