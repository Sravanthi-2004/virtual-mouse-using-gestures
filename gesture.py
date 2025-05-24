import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0
smoothening = 7

click_down = False
last_double_click_time = 0

def fingers_up_status(lm):
    """
    Returns list of booleans: True if finger is up, False if down.
    Order: [Thumb, Index, Middle, Ring, Pinky]
    """
    fingers = []
    # Thumb: compare tip and IP joint x coords (right hand assumption)
    if lm[4].x < lm[3].x:
        fingers.append(True)
    else:
        fingers.append(False)
    # Other fingers: tip y < pip y means finger is up
    for tip, pip in [(8,6), (12,10), (16,14), (20,18)]:
        fingers.append(lm[tip].y < lm[pip].y)
    return fingers

def distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    action_text = "No Gesture"

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark
        fingers = fingers_up_status(lm)

        # Index finger tip position for cursor move
        ix, iy = int(lm[8].x * w), int(lm[8].y * h)
        screen_x = np.interp(ix, (0, w), (0, screen_w))
        screen_y = np.interp(iy, (0, h), (0, screen_h))

        current_time = time.time()

        # Gesture 1: Move cursor (index finger up only)
        if fingers[1] and not any([fingers[0], fingers[2], fingers[3], fingers[4]]):
            prev_x += (screen_x - prev_x) / smoothening
            prev_y += (screen_y - prev_y) / smoothening
            pyautogui.moveTo(prev_x, prev_y)
            action_text = "Move Cursor 👆"

        # Gesture 2: Left Click (thumb and index tips close)
        dist_thumb_index = distance(lm[4], lm[8])
        if dist_thumb_index < 0.05:
            if not click_down:
                pyautogui.click()
                click_down = True
                action_text = "Left Click 🖱️"
        else:
            click_down = False

        # Gesture 3: Right Click (thumb up only)
        if fingers[0] and not any(fingers[1:]):
            pyautogui.rightClick()
            action_text = "Right Click 🖱️(Right)"
            time.sleep(0.3)

        # Gesture 4: Scroll Up (all fingers up)
        if all(fingers):
            pyautogui.scroll(20)
            action_text = "Scroll Up 🔃"
            time.sleep(0.3)

        # Gesture 5: Scroll Down (fist)
        if not any(fingers):
            pyautogui.scroll(-20)
            action_text = "Scroll Down 🔽"
            time.sleep(0.3)

        # Gesture 6: Double Click (index + middle up only)
        if fingers[1] and fingers[2] and not fingers[0] and not fingers[3] and not fingers[4]:
            if current_time - last_double_click_time > 1:
                pyautogui.doubleClick()
                action_text = "Double Click ⏩🖱️"
                last_double_click_time = current_time

        # Gesture 7: Volume Up (only pinky up)
        if fingers[4] and not any(fingers[:4]):
            pyautogui.press("volumeup")
            action_text = "Volume Up 🔊"
            time.sleep(0.5)

        # Gesture 8: Volume Down (only ring up)
        if fingers[3] and not any([fingers[0], fingers[1], fingers[2], fingers[4]]):
            pyautogui.press("volumedown")
            action_text = "Volume Down 🔉"
            time.sleep(0.5)

        # Gesture 9: Minimize Window (thumb + pinky up only)
        if fingers[0] and fingers[4] and not any(fingers[1:4]):
            pyautogui.hotkey('win', 'down')
            action_text = "Minimize Window 🪟⬇️"
            time.sleep(0.5)

        # Gesture 10: Mute/Unmute Volume (thumb + ring + pinky up only)
        if fingers[0] and fingers[3] and fingers[4] and not fingers[1] and not fingers[2]:
            pyautogui.press("volumemute")
            action_text = "Mute/Unmute 🔇"
            time.sleep(0.5)

        # Gesture 11: Lock Screen (index + pinky up only)
        if fingers[1] and fingers[4] and not fingers[0] and not fingers[2] and not fingers[3]:
            pyautogui.hotkey('win', 'l')
            action_text = "Lock Screen 🔒"
            time.sleep(1)

        # Gesture 12: Open File Explorer (middle + ring up only)
        if fingers[2] and fingers[3] and not fingers[0] and not fingers[1] and not fingers[4]:
            pyautogui.hotkey('win', 'e')
            action_text = "Open File Explorer 📁"
            time.sleep(1)

        # Gesture 13: Open Calculator (thumb + index + middle up only)
        if fingers[0] and fingers[1] and fingers[2] and not fingers[3] and not fingers[4]:
            pyautogui.hotkey('win', 'r')  # open run dialog
            time.sleep(0.2)
            pyautogui.write('calc')
            pyautogui.press('enter')
            action_text = "Open Calculator 🧮"
            time.sleep(1)

        # Gesture 14: Close Window (thumb + index + pinky up only)
        if fingers[0] and fingers[1] and fingers[4] and not fingers[2] and not fingers[3]:
            pyautogui.hotkey('alt', 'f4')
            action_text = "Close Window ❌"
            time.sleep(1)

        # Gesture 15: Refresh Page (thumb + ring + pinky up only)
        if fingers[0] and fingers[3] and fingers[4] and not fingers[1] and not fingers[2]:
            pyautogui.press('f5')
            action_text = "Refresh Page 🔄"
            time.sleep(1)

        mp_drawing.draw_landmarks(img, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

    cv2.putText(img, action_text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow("Virtual Mouse - Full Gestures", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
