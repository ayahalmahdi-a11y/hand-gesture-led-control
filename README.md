# ✋💡 Hand Gesture LED Control

Control LEDs with your bare hand! A webcam tracks your hand, counts how many fingers you're holding up, and an Arduino lights up that many LEDs.

Built as a midterms distraction project. Idea inspired by Arwa's project on TikTok. 🙌

## How it works

1. **Python + OpenCV + MediaPipe** track your hand through the webcam and count the raised fingers.
2. The finger count (0 to 5) is sent to the Arduino over **serial** (9600 baud).
3. The **Arduino UNO** reads the number and turns on that many LEDs.
4. If no hand is detected, all LEDs turn off.

```
Webcam → MediaPipe (finger count) → Serial → Arduino UNO → LEDs
```

## Hardware

- Arduino UNO
- Breadboard
- 5 LEDs
- 5 resistors (220 Ω is a common choice)
- Jumper wires
- USB cable
- Laptop with a webcam

### Wiring

| LED | Arduino Pin |
|-----|-------------|
| LED 1 | 8 |
| LED 2 | 9 |
| LED 3 | 10 |
| LED 4 | 11 |
| LED 5 | 12 |

Each LED connects through a resistor to GND.

## Software requirements

- Python 3.8+
- [Arduino IDE](https://www.arduino.cc/en/software)
- Python libraries:

```bash
pip install opencv-python mediapipe pyserial
```

## Setup and usage

1. Wire the circuit as shown above.
2. Open `controlling_leds_with_my_hand_gg.ino` in the Arduino IDE and upload it to your Arduino UNO.
3. Close the Arduino Serial Monitor, since it blocks the port.
4. In `hand_led_control.py`, change the serial port to match yours (for example `COM6` on Windows, or `/dev/ttyACM0` on Linux):

   ```python
   arduino = serial.Serial("COM6", 9600, timeout=1)
   ```

5. Run the Python script:

   ```bash
   python hand_led_control.py
   ```

6. Show your hand to the camera and hold up 0 to 5 fingers. Press **Q** to quit.

## Project structure

```
├── controlling_leds_with_my_hand_gg.ino   # Arduino code
├── hand_led_control.py                    # Python hand tracking code
└── README.md
```

## Tech stack

Python, OpenCV, MediaPipe, PySerial, Arduino C++

## Demo

Add your demo video or GIF here, for example:

```
![Demo](demo.gif)
```

## Credits

Idea by Arwa. This is my own version of it.
