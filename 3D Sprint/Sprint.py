import serial
import serial.tools.list_ports
import pygame
import sys

# Auto-detect Bluetooth COM port
ports = list(serial.tools.list_ports.comports())
bt_port = None
for p in ports:
    if "Bluetooth" in p.description or "ESP32" in p.description:
        bt_port = p.device
        break

if not bt_port:
    print("Bluetooth device not found!")
    sys.exit()

# Open the serial port (must match Arduino Bluetooth baud rate)
bt = serial.Serial(bt_port, 38400, timeout=1)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bluetooth Joystick Control")

# Initial circle position
x, y = 300, 300
clock = pygame.time.Clock()
circle_color = (0, 255, 0)  # Green

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bt.close()
            pygame.quit()
            sys.exit()

    # Read data from Bluetooth
    if bt.in_waiting:
        try:
            line = bt.readline().decode().strip()
            dx, dy, btn = map(int, line.split(','))

            # Map joystick 0–1023 to smooth movement
            x += (dx - 512) / 50
            y -= (dy - 512) / 50  # invert Y-axis

            # Button changes circle color
            circle_color = (255, 0, 0) if btn == 0 else (0, 255, 0)
        except:
            pass

    # Keep circle inside screen boundaries
    x = max(20, min(580, x))
    y = max(20, min(580, y))

    # Draw circle
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, (int(x), int(y)), 20)
    pygame.display.flip()
    clock.tick(30)
