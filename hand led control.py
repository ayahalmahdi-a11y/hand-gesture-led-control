import cv2
import mediapipe as mp
import serial
import time

arduino = serial.Serial("COM6", 9600, timeout=1)
time.sleep(2)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
camera = cv2.VideoCapture(0)

cv2.namedWindow("Hand LED Control", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hand LED Control", 320, 240)
last_command = None

def count_fingers(hand_landmarks, handedness):
    points = hand_landmarks.landmark
    fingers = 0
    
    if handedness == "Right":
        if points[4].x < points[3].x:
            fingers += 1
    else:
        if points[4].x > points[3].x:
            fingers += 1
    
    finger_tips = [8, 12, 16, 20]
    finger_joints = [6, 10, 14, 18]
    for tip, joint in zip(finger_tips, finger_joints):
        if points[tip].y < points[joint].y:
            fingers += 1
    return fingers

try:
    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        fingers = 0
        if results.multi_hand_landmarks:
            for index, hand_landmarks in enumerate(
                results.multi_hand_landmarks
            ):
                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )
                handedness = (
                    results.multi_handedness[index]
                    .classification[0].label
                )
                fingers = count_fingers(
                    hand_landmarks,
                    handedness
                )
            
            if fingers != last_command:
                arduino.write(str(fingers).encode())
                last_command = fingers
            text = f"Fingers: {fingers}"
        else:
            
            if last_command != 0:
                arduino.write(b"0")
                last_command = 0
            text = "No hand detected"
        cv2.putText(
            frame,
            text,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
        cv2.imshow("Hand LED Control", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    hands.close()
    arduino.close()
    cv2.destroyAllWindows()
