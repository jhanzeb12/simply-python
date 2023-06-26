from abc import ABCMeta, abstractmethod

class IVehicle(metaclass=ABCMeta):

    vehicle_type = None
    vehicle_capacity = 1

    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    @abstractmethod
    def set_vehicle_capacity(self, capacity: int):
        """ Method to set vehical capacity e.g. 4 persons, 5 persons"""

    def get_vehicle_details(self):
        print(f"Get Vehicle Details of Abstract Class")
        return ({
            "vehicle_type": self.vehicle_type,
            "vehicle_capacity": self.vehicle_capacity
        })
