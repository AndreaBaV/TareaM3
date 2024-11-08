# semaforo.py

class Semaforo:
    def __init__(self, posicion, duracion_rojo=5, duracion_verde=5, duracion_amarillo=2):
        self.posicion = posicion
        self.duracion_rojo = duracion_rojo
        self.duracion_verde = duracion_verde
        self.duracion_amarillo = duracion_amarillo
        self.tiempo_actual = 0
        self.estado = 'rojo'

    def actualizar(self, tiempo_actual):
        tiempo_delta = tiempo_actual - self.tiempo_actual
        if self.estado == 'rojo' and tiempo_delta >= self.duracion_rojo:
            self.estado = 'verde'
            self.tiempo_actual = tiempo_actual
        elif self.estado == 'verde' and tiempo_delta >= self.duracion_verde:
            self.estado = 'amarillo'
            self.tiempo_actual = tiempo_actual
        elif self.estado == 'amarillo' and tiempo_delta >= self.duracion_amarillo:
            self.estado = 'rojo'
            self.tiempo_actual = tiempo_actual

    def obtener_color(self):
        if self.estado == 'rojo':
            return (1, 0, 0)
        elif self.estado == 'amarillo':
            return (1, 1, 0)
        elif self.estado == 'verde':
            return (0, 1, 0)
