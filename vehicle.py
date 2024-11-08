from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Vehicle:
    def __init__(self, lane, tamCelda, direction='straight'):
        self.lane = lane
        self.direction = direction
        self.tamCelda = tamCelda
        self.position = [tamCelda * (1 if lane == 'A' else -1), 0, 0]
        self.speed = 0.05

    def update_position(self):
        if self.lane == 'A':
            self.position[0] += self.speed
        else:
            self.position[0] -= self.speed

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        
        # Draw car body
        glColor3f(0.2, 0.2, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.2 * self.tamCelda, -0.1 * self.tamCelda, 0.05)
        glVertex3f(0.2 * self.tamCelda, -0.1 * self.tamCelda, 0.05)
        glVertex3f(0.2 * self.tamCelda, 0.1 * self.tamCelda, 0.05)
        glVertex3f(-0.2 * self.tamCelda, 0.1 * self.tamCelda, 0.05)
        glEnd()

        # Draw car cabin
        glColor3f(0.0, 0.6, 0.8)
        glBegin(GL_QUADS)
        glVertex3f(-0.1 * self.tamCelda, -0.05 * self.tamCelda, 0.15)
        glVertex3f(0.1 * self.tamCelda, -0.05 * self.tamCelda, 0.15)
        glVertex3f(0.1 * self.tamCelda, 0.05 * self.tamCelda, 0.15)
        glVertex3f(-0.1 * self.tamCelda, 0.05 * self.tamCelda, 0.15)
        glEnd()

        # Draw wheels
        glColor3f(0.1, 0.1, 0.1)
        glBegin(GL_QUADS)
        glVertex3f(-0.15 * self.tamCelda, -0.12 * self.tamCelda, 0.02)
        glVertex3f(-0.05 * self.tamCelda, -0.12 * self.tamCelda, 0.02)
        glVertex3f(-0.05 * self.tamCelda, -0.1 * self.tamCelda, 0.02)
        glVertex3f(-0.15 * self.tamCelda, -0.1 * self.tamCelda, 0.02)
        glEnd()
        
        glBegin(GL_QUADS)
        glVertex3f(0.15 * self.tamCelda, -0.12 * self.tamCelda, 0.02)
        glVertex3f(0.05 * self.tamCelda, -0.12 * self.tamCelda, 0.02)
        glVertex3f(0.05 * self.tamCelda, -0.1 * self.tamCelda, 0.02)
        glVertex3f(0.15 * self.tamCelda, -0.1 * self.tamCelda, 0.02)
        glEnd()
        
        glPopMatrix()
