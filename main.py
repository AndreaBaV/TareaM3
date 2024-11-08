# main.py

import argparse
import datetime
import display  # Importa la visualización y semáforo
from report import generate_report  # Genera el reporte

def main():
    parser = argparse.ArgumentParser(description="Intersection Simulation")
    
    # Argumentos para la simulación
    parser.add_argument("--M", required=True, type=int, help="Número de filas")
    parser.add_argument("--N", required=True, type=int, help="Número de columnas")
    parser.add_argument("--vehicles", required=True, type=int, help="Número de vehículos a simular")
    parser.add_argument("--t", required=True, type=int, help="Tiempo de espera para el semáforo (en segundos)")
    parser.add_argument("--n", required=True, type=int, help="Umbral de vehículos para cruzar en el carril B")

    Options = parser.parse_args()
    results = display.main(Options)  # Ejecuta la visualización y obtiene los resultados

    generate_report(results)  # Genera un reporte de la simulación

if __name__ == "__main__":
    print("\n[start] " + str(datetime.datetime.now()) + "\n")
    main()
    print("\n[end] " + str(datetime.datetime.now()) + "\n")
