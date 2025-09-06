# 🚗 Smart License Plate Recognition & Door Control System

This project uses a webcam and Optical Character Recognition (OCR) to detect a vehicle's license plate in real-time.  
If the detected plate matches a list of authorized IDs, the system simulates opening a door (e.g., a garage, gate, etc.).

Later versions will support **face recognition** for extra security. (in progress)

---

## 🔧 Features

- Real-time video stream from any camera (e.g., webcam)
- License plate text detection using EasyOCR
- Access control: only authorized plates are allowed
- Automatically stops recording once a match is found
- Placeholder for physical "door opening" (simulated via terminal print)
- Modular Python code ready for hardware integration (e.g., Raspberry Pi, relay module)

---

## 🧠 How It Works

1. Webcam captures frames in real-time
2. EasyOCR scans the image for any text
3. The system checks if any detected text matches known plate numbers
4. If a match is found:
   - The system prints a success message
   - Simulates opening the door
   - Stops the camera feed

---

## 🚀 Getting Started

### 1. Install Requirements

You can install the dependencies using `pip`:

```bash
pip install opencv-python easyocr imutils
