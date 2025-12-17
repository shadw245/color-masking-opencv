import cv2
import numpy as np

# Open camera (0 = default webcam)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize (optional but smoother)
    frame = cv2.resize(frame, (640, 480))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # === STRICT RED RANGES (NO ORANGE) ===
    lower_red1 = np.array([0, 150, 90])
    upper_red1 = np.array([6, 255, 255])

    lower_red2 = np.array([174, 150, 90])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 | mask2

    # Morphological cleaning
    kernel = np.ones((3, 3), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)

    # Apply mask
    red_only = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Display
    cv2.imshow("Original Video", frame)
    cv2.imshow("Red Mask", red_mask)
    cv2.imshow("Live Red Tracking", red_only)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
