
# 🎯 Virtual Mouse Using Gestures

A **real-time hand gesture recognition system** that allows users to control mouse and system functions using only their hands. This touchless interface enhances **accessibility, hygiene, and interaction** in smart environments.

---

## 📌 Overview

This project uses a **webcam**, **MediaPipe**, **OpenCV**, and **PyAutoGUI** to:

* Detect hand landmarks
* Recognize predefined hand gestures
* Simulate mouse and system control actions

---

## 🚀 Features

✅ Real-time gesture recognition
✅ 15+ gesture-based system actions
✅ Contactless control for hygiene and accessibility
✅ Seamless integration using Python

---

## 🛠️ System Architecture

### 🔧 Components:

* **Webcam** – For live video feed
* **MediaPipe** – For accurate hand landmark detection
* **OpenCV** – For image processing and visualization
* **PyAutoGUI** – For simulating keyboard/mouse input

### 🔄 Workflow:

1. Capture video from the webcam
2. Detect hand landmarks using **MediaPipe**
3. Recognize gestures using finger positions
4. Simulate appropriate actions using **PyAutoGUI**

---

## 📊 Block Diagram

         +------------------+
         |     Webcam       |
         |  (Live Feed)     |
         +--------+---------+
                  |
                  v
         +------------------+
         |   OpenCV         |
         | (Frame Capture & |
         |  Preprocessing)  |
         +--------+---------+
                  |
                  v
         +------------------+
         |   MediaPipe      |
         | (Hand Landmark   |
         |   Detection)     |
         +--------+---------+
                  |
                  v
         +---------------------------+
         |   Gesture Recognition     |
         | (Analyze finger positions |
         |  & map to defined gestures)|
         +------------+--------------+
                      |
                      v
         +----------------------------+
         |   PyAutoGUI Actions        |
         | (Mouse & System Simulation)|
         +----------------------------+


---

## ✋ Gesture Mapping

| Gesture                | Action             |
| ---------------------- | ------------------ |
| Index Up               | Move Cursor        |
| Thumb + Index Close    | Left Click         |
| Thumb Up               | Right Click        |
| All Fingers Up         | Scroll Up          |
| Fist                   | Scroll Down        |
| Index + Middle Up      | Double Click       |
| Pinky Up               | Volume Up          |
| Ring Up                | Volume Down        |
| Thumb + Pinky          | Minimize Window    |
| Thumb + Ring + Pinky   | Toggle Mute        |
| Index + Pinky          | Lock Screen        |
| Middle + Ring          | Open File Explorer |
| Thumb + Index + Middle | Open Calculator    |
| Thumb + Index + Pinky  | Close Window       |
| Thumb + Ring + Pinky   | Refresh Page       |

---

## ✅ Advantages

* ⚡ **Real-time**, low-latency gesture detection
* 🎯 High accuracy with **MediaPipe**
* 🧼 **Touchless interface** — ideal for cleanrooms, public kiosks
* 💼 Useful for **presentations**, **accessibility tools**, **smart environments**

---

## 📷 Output Screenshots

![ChatGPT Image May 24, 2025, 10_49_24 PM](https://github.com/user-attachments/assets/a0e2b325-03d9-41ec-b753-f6b6ee29f212)


---

## 🧑‍💻 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/virtual-mouse-using-gestures.git
cd virtual-mouse-using-gestures
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python main.py
```

---

## 📚 Requirements

* Python 3.7+
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

---

## 📦 Future Enhancements

* Add dynamic gesture recording
* Support multi-hand input
* GUI to toggle gesture mappings

---

## 🙌 Acknowledgments

* [MediaPipe](https://google.github.io/mediapipe/) by Google
* [OpenCV](https://opencv.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/)

---


