EYE CONTROLLED MOUSE PROJECT

This project uses OpenCV, MediaPipe, and PyAutoGUI to control the mouse cursor with eye movements.
It captures video from the webcam, processes it to detect facial landmarks, and uses specific eye 
landmarks to move the mouse cursor and perform clicks.

Installation
1. Clone the repository on your pc:
    ```bash
    git clone https://github.com/yourusername/eye-control-mouse.git
    cd eye-control-mouse
    ```

2. Install the required packages:
    1. open the project folder from command line and run the code below:
    pip install -r requirements.txt



USAGE
1. Run the script:
    ```bash
    python main.py
    ```

2. The script will open your webcam and start tracking your eyes. Move your eyes to control the mouse cursor.
What's happending when the program is running:
- The webcam captures video frames.
- MediaPipe Face Mesh detects facial landmarks.
- The script calculates the coordinates of specific eye landmarks.
- PyAutoGUI moves the mouse cursor based on the calculated coordinates.
- Blinking is detected to perform mouse clicks.

Requirements
python 3.8 - Python 3.10 versions only can be used for this project

Troubleshooting
- Ensure your webcam is connected and accessible.
- If the camera feed is laggy, try reducing the frame resolution or optimizing the code.

Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

License
This project is licensed under the KNUST License.

Acknowledgements
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)

Author
Theophilus Arkoh