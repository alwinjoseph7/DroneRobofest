import sys
import cv2
import apriltag

def read_cam():
    cap = cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480 ! videoconvert ! video/x-raw,format=BGR ! appsink")
    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, img = cap.read();
            cv2.imshow('demo',img)
            cv2.waitKey(10)

            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            result = apriltag.Detector().detect(img_gray)
            if result:
                print result[0][1]
    else:
     print "camera open failed"

    cv2.destroyAllWindows()

if __name__ == '__main__':
    read_cam()