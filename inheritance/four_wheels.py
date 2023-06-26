from inheritance.abstract_vehicle import IVehicle

class FourWheels(IVehicle):

    def __init__(self):
        self.vehicle_type = "Four Wheels"

    def set_vehicle_capacity(self, capacity: int):
        if capacity < 1:
            print("Vehicle Capacity cannot be less than 1")
        else:
            self.vehicle_capacity = capacity
