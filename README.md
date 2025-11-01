Bluetooth Joystick Control with Arduino and Pygame
Overview

This project allows you to control a circle in a Python Pygame window using an analog joystick connected to an Arduino. The Arduino reads X/Y axis values and a button press and transmits the data via Bluetooth to a PC. A Python script automatically detects the Bluetooth COM port, reads the joystick data, and updates the circle’s position and color in real-time.

This project demonstrates:

Serial communication between Arduino and PC.

Wireless data transmission using Bluetooth.

Joystick input handling with analog values and button presses.

Pygame graphics for real-time visualization.

Features

Smooth movement of a circle based on joystick analog input.

Automatic detection of the active Bluetooth COM port.

Circle changes color when the joystick button is pressed.

Keeps the circle within the Pygame window boundaries.

Easy to customize sensitivity and window size.

Hardware Requirements

Arduino Uno, Nano, or compatible board.

Analog joystick module (X/Y axes + button).

Bluetooth module (HC-05, HC-06, or ESP32).

Jumper wires and breadboard.

Connections
Arduino Pin	Component	Notes
A0	Joystick X	Analog X-axis
A1	Joystick Y	Analog Y-axis
D2	Joystick SW	Button (INPUT_PULLUP)
10	Bluetooth RX	SoftwareSerial RX
11	Bluetooth TX	SoftwareSerial TX
Software Requirements

Arduino IDE

Python 3.x

Python libraries: pyserial, pygame

Install Python dependencies:

pip install pyserial pygame

Arduino Sketch

The Arduino reads joystick values and sends them via Bluetooth in comma-separated format:

x_value,y_value,button_value


x_value and y_value: 0–1023 (analog reading)

button_value: 0 when pressed, 1 when released

Sample Arduino code snippet:

int x = analogRead(A0);
int y = analogRead(A1);
int button = digitalRead(2);
Serial.println(String(x) + "," + String(y) + "," + String(button));


Full Arduino sketch should also include SoftwareSerial to communicate with the Bluetooth module.

Python Script

The Python script:

Auto-detects the Bluetooth COM port.

Reads joystick data in real-time.

Maps analog joystick values (0–1023) to movement in Pygame window.

Changes circle color when button is pressed.

Sample Python snippet:

dx, dy, btn = map(int, line.split(','))
x += (dx - 512) / 50
y -= (dy - 512) / 50
circle_color = (255, 0, 0) if btn == 0 else (0, 255, 0)

Usage

Upload the Arduino sketch to your board.

Power your Bluetooth module and pair it with your PC.

Run the Python script:

python joystick_bt.py


The circle should move according to your joystick.

Pressing the joystick button changes the circle color.

Customization

Sensitivity: Adjust (dx-512)/50 and (dy-512)/50 in Python to change movement speed.

Window size: Change pygame.display.set_mode((600,600)) to your desired resolution.

Button action: Add custom actions in Python when btn == 0.

How It Works

Arduino continuously reads analog X/Y and button values.

Arduino sends the values via Bluetooth using SoftwareSerial.

Python detects the Bluetooth port automatically.

Python reads the CSV-formatted joystick data.

The Pygame circle updates its position based on the mapped X/Y values.

The circle changes color when the joystick button is pressed.

Screenshots


Circle movement and button color change demonstration

License

This project is open-source and available under the MIT License.
