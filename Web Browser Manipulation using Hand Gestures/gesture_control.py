import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Variables to track gesture
previous_positions = {}
gesture_triggered = False
last_gesture_time = time.time()
gesture_timeout = 1.0  # Timeout in seconds to prevent multiple gestures in quick succession

def left_tab_switch():
    """Function to switch to the previous tab in Chrome."""
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(0.2)  # Small delay to allow tab to switch

def right_tab_switch():
    """Function to switch to the next tab in Chrome."""
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.2)  # Small delay to allow tab to switch

def scroll_up():
    """Function to scroll up the current page."""
    pyautogui.scroll(200)
    time.sleep(0.2)  # Small delay to allow scroll to apply

def scroll_down():
    """Function to scroll down the current page."""
    pyautogui.scroll(-200)
    time.sleep(0.2)  # Small delay to allow scroll to apply

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to avoid mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Check if any hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the positions of the index and middle fingertips
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Get the position of the wrist landmark
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Initialize previous positions if this is the first detection
            if not previous_positions:
                previous_positions = {
                    'index_finger_tip': index_finger_tip.x,
                    'middle_finger_tip': middle_finger_tip.x,
                    'wrist': wrist.y
                }

            # Detect left and right swipes for tab switching
            if abs(previous_positions['index_finger_tip'] - index_finger_tip.x) > 0.1 and \
               abs(previous_positions['middle_finger_tip'] - middle_finger_tip.x) > 0.1:
                if not gesture_triggered:
                    current_time = time.time()
                    if current_time - last_gesture_time > gesture_timeout:
                        if previous_positions['index_finger_tip'] > index_finger_tip.x and \
                           previous_positions['middle_finger_tip'] > middle_finger_tip.x:
                            print("Two-finger swipe left detected! Switching to previous tab.")
                            left_tab_switch()
                        elif previous_positions['index_finger_tip'] < index_finger_tip.x and \
                             previous_positions['middle_finger_tip'] < middle_finger_tip.x:
                            print("Two-finger swipe right detected! Switching to next tab.")
                            right_tab_switch()
                        gesture_triggered = True
                        last_gesture_time = current_time
                        time.sleep(0.5)  # Wait for 0.5 seconds to avoid multiple triggers

            # Detect up and down hand movements for scrolling
            if abs(previous_positions['wrist'] - wrist.y) > 0.1:
                if not gesture_triggered:
                    current_time = time.time()
                    if current_time - last_gesture_time > gesture_timeout:
                        if previous_positions['wrist'] > wrist.y:
                            print("Hand moved up! Scrolling up.")
                            scroll_up()
                        elif previous_positions['wrist'] < wrist.y:
                            print("Hand moved down! Scrolling down.")
                            scroll_down()
                        gesture_triggered = True
                        last_gesture_time = current_time
                        time.sleep(0.5)  # Wait for 0.5 seconds to avoid multiple triggers

            # Update previous positions for the next frame
            previous_positions = {
                'index_finger_tip': index_finger_tip.x,
                'middle_finger_tip': middle_finger_tip.x,
                'wrist': wrist.y
            }

        # Reset gesture trigger if fingers are not moving
        if abs(previous_positions['index_finger_tip'] - index_finger_tip.x) < 0.01 and \
           abs(previous_positions['middle_finger_tip'] - middle_finger_tip.x) < 0.01 and \
           abs(previous_positions['wrist'] - wrist.y) < 0.01:
            gesture_triggered = False

    # Display the frame
    #cv2.imshow("Gesture Control Demo", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
