import numpy as np
import face_recognition
import cv2
from simple_facerec import SimpleFacerec
cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("Frame",frame)
    

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()