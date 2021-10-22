import cv2

cap=cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    objects,_,_=cv2.QRCodeDetector().detectAndDecode(frame)
    cv2.imshow("frame", frame)
    if objects != '':
        print("Detected")
    else:
        print("Not Detected")
    if cv2.waitKey(1) & 0xFF != ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
