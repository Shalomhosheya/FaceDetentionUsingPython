import cv2
import numpy as np
import screen_brightness_control as sbc  # Library to control screen brightness

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

# Set default brightness level
DEFAULT_BRIGHTNESS = sbc.get_brightness(display=0)[0]  # Get current brightness
HIGH_BRIGHTNESS = min(DEFAULT_BRIGHTNESS + 40, 100)    # Increase brightness when face detected

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for better face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        sbc.set_brightness(HIGH_BRIGHTNESS, display=0)  # Increase screen brightness
    else:
        sbc.set_brightness(DEFAULT_BRIGHTNESS, display=0)  # Reset brightness

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection with Brightness Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Reset brightness to default before exiting
sbc.set_brightness(DEFAULT_BRIGHTNESS, display=0)

cap.release()
cv2.destroyAllWindows()
