# Gesture-Controlled Browser Navigation

This project enables users to control their web browser using hand gestures captured through a webcam. It uses **MediaPipe** for hand tracking and **PyAutoGUI** for simulating keyboard and mouse actions.

## Features

- **Tab Switching**:
  - **Swipe Left**: Switch to the previous browser tab (`Ctrl + Shift + Tab`).
  - **Swipe Right**: Switch to the next browser tab (`Ctrl + Tab`).

- **Scrolling**:
  - **Move Hand Up**: Scroll up the current page.
  - **Move Hand Down**: Scroll down the current page.

- **Real-Time Hand Tracking**:
  - Visualizes hand landmarks on the video feed using MediaPipe.

## How It Works

1. **Hand Tracking**:
   - The program captures video input from the webcam.
   - MediaPipe detects and tracks hand landmarks.

2. **Gesture Detection**:
   - **Swipe Gestures**:
     - Detects two-finger (index and middle) horizontal swipes for tab switching.
   - **Vertical Movements**:
     - Tracks wrist movements to scroll up or down.

3. **Browser Control**:
   - PyAutoGUI simulates keyboard and mouse actions based on detected gestures.

## Usage

1. Start the program.
2. Perform the following gestures in front of the webcam:
   - **Swipe Left (Two Fingers)**: Switch to the previous browser tab.
   - **Swipe Right (Two Fingers)**: Switch to the next browser tab.
   - **Move Hand Up**: Scroll up.
   - **Move Hand Down**: Scroll down.
3. Press `q` to exit the program.

## Limitations

- Only detects one hand at a time.
- Requires a consistent gesture for accurate detection.
- May not work reliably in low-light conditions or with poor webcam quality.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [MediaPipe](https://google.github.io/mediapipe/) for its robust hand-tracking solution.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for simulating keyboard and mouse actions.
