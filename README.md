#  Live Red Color Masking using OpenCV

This project demonstrates **real-time red color detection** using **OpenCV** and **Python**.
It captures video from a webcam, converts frames to HSV color space, and applies strict
red color masking to avoid detecting orange or other similar colors.

---

##  Project Structure
color-masking-opencv/
│
├── pics/ # Sample images
│ ├── red2.jpg
│ ├── red3.jpg
│ ├── red4.png
│ └── red5.jpg
│
├── assignment_color_masking.ipynb
├── color.ipynb # Notebook for image-based color masking
├── live.py # Real-time webcam red detection
└── README.md


---

##  How It Works

1. Capture live video from the webcam
2. Resize frames for smoother processing
3. Convert frames from **BGR → HSV**
4. Apply **two strict HSV ranges** for red color
5. Combine masks and clean noise using morphology
6. Display:
   - Original video
   - Red mask
   - Red-only output

---
## Run the Live Red Detection
```bash
python live.py
```

Press ESC to exit the camera window.
##  Requirements

Make sure you have Python installed, then install dependencies:

```bash
pip install opencv-python numpy
```

---

## Run the Live Red Detection
```bash
python live.py
```
Press ESC to exit the camera window.

---

##  Jupyter Notebook

color.ipynb contains color masking applied to **static images** for testing and visualization.
