import numpy as np
import cv2
from PIL import Image

from util import get_limits

cap = cv2.VideoCapture(0)
yellow = [0, 255, 255]
while True:
    ret, frame = cap.read()

    lowerLimit, upperLimit = get_limits(color=yellow)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    cv2.imshow('frame', frame)

    # 0xFF for platform independency
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()