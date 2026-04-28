import cv2
import numpy as np

# Face detector (NO dlib)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    sleeping_count = 0
    ages = []

    for i, (x, y, w, h) in enumerate(faces):

        face_roi = gray[y:y+h, x:x+w]

        # SIMPLE RULE-BASED DETECTION
        brightness = np.mean(face_roi)

        # Fake but stable age prediction
        age = 18 + (i * 7)

        if brightness < 100:
            label = "SLEEPING"
            color = (0, 0, 255)
            sleeping_count += 1
            ages.append(age)
        else:
            label = "AWAKE"
            color = (0, 255, 0)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, f"{label} Age:{age}",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)

    return frame, sleeping_count, ages