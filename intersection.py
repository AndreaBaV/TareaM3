import random
import time
from trafficLight import TrafficLight
from vehicle import Vehicle

class Intersection:
    def __init__(self, trafficLight, vehicle_rate_A, vehicle_rate_B):
        self.trafficLight = trafficLight
        self.vehicles_A = []
        self.vehicles_B = []
        self.vehicle_rate_A = vehicle_rate_A
        self.vehicle_rate_B = vehicle_rate_B

    def spawn_vehicle(self, lane):
        direction = 'left' if random.random() < 0.3 else 'straight'
        vehicle = Vehicle(lane, direction)
        if lane == 'A':
            self.vehicles_A.append(vehicle)
        else:
            self.vehicles_B.append(vehicle)

    def update_vehicles(self):
        for vehicle in self.vehicles_A:
            vehicle.update_position()
        for vehicle in self.vehicles_B:
            vehicle.update_position()

    def render(self):
        for vehicle in self.vehicles_A + self.vehicles_B:
            vehicle.draw()
