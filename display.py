import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from piso import Celdas
from semaforo import Semaforo
from vehicle import Vehicle
import time
import csv

def draw_board(matriz_celdas, tamCelda, semaforo, vehicles):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    M, N = len(matriz_celdas), len(matriz_celdas[0])
    gluLookAt(M * tamCelda / 2, -N * tamCelda / 2, M * tamCelda,
              M * tamCelda / 2, N * tamCelda / 2, 0,
              0, 0, 1)

    # Draw the grid and avenues
    for row in matriz_celdas:
        for cell in row:
            x, y = cell.posicion[1] * tamCelda, cell.posicion[0] * tamCelda
            # Define avenue cells
            if cell.posicion[1] == N // 2 or cell.posicion[0] == M // 2:
                glColor3f(0.5, 0.5, 0.5)
            else:
                glColor3f(0.8, 0.8, 0.8)
            glBegin(GL_QUADS)
            glVertex3f(x, y, 0)
            glVertex3f(x + tamCelda, y, 0)
            glVertex3f(x + tamCelda, y + tamCelda, 0)
            glVertex3f(x, y + tamCelda, 0)
            glEnd()

    # Draw vehicles and traffic light
    for vehicle in vehicles:
        vehicle.draw()
    glColor3f(*semaforo.obtener_color())
    x, y = semaforo.posicion[1] * tamCelda, semaforo.posicion[0] * tamCelda
    glBegin(GL_QUADS)
    glVertex3f(x, y, 0.1)
    glVertex3f(x + tamCelda, y, 0.1)
    glVertex3f(x + tamCelda, y + tamCelda, 0.1)
    glVertex3f(x, y + tamCelda, 0.1)
    glEnd()
    pygame.display.flip()

def main(Options):
    pygame.init()
    tamCelda = min(800 // Options.M, 800 // Options.N)
    pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, Options.M * tamCelda * 4)
    glMatrixMode(GL_MODELVIEW)

    matriz_celdas = Celdas.matrizPosiciones(Options)
    semaforo = Semaforo(posicion=(Options.M // 2, Options.N // 2))
    vehicles = [Vehicle(lane='A', tamCelda=tamCelda) for _ in range(Options.vehicles)]
    start_time = time.time()
    data = []

    running = True
    while running and time.time() - start_time < Options.t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tiempo_actual = pygame.time.get_ticks() / 1000
        semaforo.actualizar(tiempo_actual)
        for vehicle in vehicles:
            vehicle.update_position()
        draw_board(matriz_celdas, tamCelda, semaforo, vehicles)

        data.append({
            "time": time.time() - start_time,
            "vehicle_count": len(vehicles),
            "semaforo_state": semaforo.estado
        })

        pygame.time.wait(100)
    pygame.quit()
    return data
