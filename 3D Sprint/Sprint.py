import serial
import serial.tools.list_ports
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
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

# Open serial port
bt = serial.Serial(bt_port, 38400, timeout=1)

# Pygame + OpenGL setup
pygame.init()
screen = pygame.display.set_mode((600, 600), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("Bluetooth Joystick 3D Cube")

gluPerspective(45, (600/600), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Initial cube position
cube_x = 0
cube_y = 0

# Cube vertices
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,7),(7,6),(6,4),
    (0,4),(1,5),(2,7),(3,6)
)

def draw_cube():
    glBegin(GL_LINES)
    glColor3f(0,1,0)  # green cube
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bt.close()
            pygame.quit()
            sys.exit()

    # Read joystick
    if bt.in_waiting:
        try:
            line = bt.readline().decode().strip()
            dx, dy, btn = map(int, line.split(','))
            cube_x += (dx - 512) / 500   # scale to OpenGL coordinates
            cube_y += (dy - 512) / 500
        except:
            pass

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(cube_x, cube_y, 0)
    draw_cube()
    glPopMatrix()
    pygame.display.flip()
    clock.tick(30)
