# Face Detection App

## Overview
This Python-based Face Detection App uses OpenCV to detect faces in images or through a webcam in real-time. The app leverages Haar Cascade classifiers, a popular method for object detection.

## Features
- Detect faces in images
- Real-time face detection using webcam
- Draws rectangles around detected faces

## Prerequisites
- Python 3.x
- OpenCV

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/face-detection-app.git
   cd face-detection-app
   ```

2. Install the required packages:
   ```bash
   pip install opencv-python
   ```

## Usage

### 1. Detect Faces in an Image
1. Place your image in the project directory.
2. Update the image file name in the Python script (`face.jpg`).
3. Run the script:
   ```bash
   python detect_faces_image.py
   ```

### 2. Real-time Face Detection using Webcam
Run the following command:
```bash
python detect_faces_webcam.py
```
Press 'q' to exit the webcam feed.

## Code Explanation
- **Haar Cascades:** Pre-trained classifiers for face detection.
- **cv2.CascadeClassifier:** Loads the cascade file.
- **detectMultiScale:** Detects objects of different sizes.
- **cv2.rectangle:** Draws rectangles around detected faces.

## Troubleshooting
- Ensure OpenCV is correctly installed.
- Verify your webcam permissions if using real-time detection.

## Contributions
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [OpenCV Documentation](https://docs.opencv.org/)
- [Haar Cascades Explained](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

## Contact
For any questions or suggestions, please contact [your-email@example.com].

