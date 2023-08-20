# HandTrack Project using OpenCV

![HandTrack Demo](demo.gif)

This project demonstrates real-time hand tracking using the OpenCV library. The goal of this project is to detect and track the movement of a hand in a video stream or webcam feed. This can be useful for various applications such as gesture recognition, virtual reality interaction, and more.

## Features

- Real-time hand detection and tracking.
- Display of bounding box around detected hand.
- Display of palm center and fingertips.
- Works with both video files and webcam feed.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

## Usage

1. Clone this repository to your local machine or download the ZIP file.

2. Navigate to the project directory:

```bash
cd HandTrack-Project
```

3. Run the `handtrack.py` script:

```bash
python handtrack.py
```

4. The script will open a window displaying the webcam feed with the hand tracking overlay. A bounding box will be drawn around the detected hand, and markers will indicate the palm center and fingertips.

5. Press the 'Q' key to exit the program.

## Customization

You can customize the behavior of the hand tracking by modifying the parameters in the `handtrack.py` script. Some of the parameters you might want to adjust include:

- `min_detection_confidence`: The minimum confidence value for a hand detection to be considered valid.
- `min_tracking_confidence`: The minimum confidence value for tracking a hand's keypoints between frames.

Feel free to experiment with these parameters to achieve the best results for your specific use case.

## Credits

This project is built upon the OpenCV library, which provides the necessary tools for real-time computer vision tasks. The hand tracking model is based on machine learning techniques and neural networks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to and expand upon this project! If you have any questions, suggestions, or improvements, please create an issue or pull request. Happy hand tracking!
