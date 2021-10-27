import cv2

cap = cv2.VideoCapture("v4l2src device=/dev/video1 ! video/x-raw, width=640, height=480 ! videoconvert ! video/x-raw,format=BGR ! appsink")
while True:
    _,frame = cap.read()
    objects,_,_=cv2.QRCodeDetector().detectAndDecode(frame)
    cv2.imshow("frame", frame)
    if objects != '':
        print("Detected")
    else:
        print("Not Detected")
    if cv2.waitKey(5) & 0xFF != ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
