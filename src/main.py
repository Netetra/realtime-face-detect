import numpy as np
import cv2
import time

def main():
    cap = cv2.VideoCapture(0);

    if not cap.isOpened():
        print("Error: Cannot open camera.")
        exit(1)

    cascade = cv2.CascadeClassifier("./assets/haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        print(faces)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y+h), (0,255,0), 4)
        
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()
