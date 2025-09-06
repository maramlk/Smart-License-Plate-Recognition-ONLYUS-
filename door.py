import cv2
import easyocr
import imutils
import time

# 1. Initialize OCR reader (English only for license plates)
reader = easyocr.Reader(['en'])

# 2. List of authorized license plates
AUTHORIZED_PLATES = ["ABC123", "123XYZ", "CAR001"]

# 3. Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

print("[INFO] Starting video stream. Looking for license plate...")

door_opened = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = imutils.resize(frame, width=800)

    # Convert to grayscale (helps with OCR accuracy)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use EasyOCR to detect text in the frame
    results = reader.readtext(gray)

    for (bbox, text, prob) in results:
        # Clean up the text
        plate_text = text.strip().upper().replace(" ", "")

        # Draw bounding box & text on frame
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(frame, plate_text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Check if plate is authorized
        if plate_text in AUTHORIZED_PLATES:
            print(f"[ACCESS GRANTED] Plate {plate_text} detected - Door opened!")
            door_opened = True
            break  # stop checking other text in frame
        else:
            print(f"[ACCESS DENIED] Plate {plate_text} not in list.")

    # Show the video feed
    cv2.imshow("License Plate Recognition", frame)

    # If door is opened, stop video feed
    if door_opened:
        print("[INFO] Stopping camera...")
        time.sleep(2)  # wait 2 seconds before closing
        break

    # Press 'q' to quit manually
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
