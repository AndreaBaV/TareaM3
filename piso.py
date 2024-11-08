# piso.py

class Celdas:
    def __init__(self, indice, posicion, agente=False, basura=False):
        self.indice = indice
        self.posicion = posicion  # Posición en el tablero
        self.agente = agente
        self.basura = basura
        self.inicial = False

    @staticmethod
    def matrizPosiciones(Options):
        M, N = Options.M, Options.N
        matriz = []
        indice = 0

        for i in range(M):
            fila = []
            for j in range(N):
                posicion = (i, j)
                celda = Celdas(indice=indice, posicion=posicion)
                fila.append(celda)
                indice += 1
            matriz.append(fila)

        return matriz
