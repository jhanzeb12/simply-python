from inheritance.four_wheels import FourWheels
from inheritance.two_wheels import TwoWheels


class ProxyVehicle:

    def __init__(self):
        self.__two_wheels = TwoWheels()
        self.__four_wheels = FourWheels()

    def get_vehicle_details(self):
        print(f"Get Vehicle Details of Proxy")
        print(self.__two_wheels.get_vehicle_details())
        print(self.__four_wheels.get_vehicle_details())

pv = ProxyVehicle()
pv.get_vehicle_details()