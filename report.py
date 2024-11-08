# report.py

import csv

def generate_report(data):
    with open('simulation_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['time', 'vehicle_count', 'semaforo_state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)
