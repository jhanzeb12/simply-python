from inheritance.four_wheels import FourWheels
from inheritance.two_wheels import TwoWheels


class VehicleFactory:

    @staticmethod
    def get_instance(vehicle_type):
        if vehicle_type == "four":
            return FourWheels()

        if vehicle_type == "two":
            return TwoWheels()

        return Exception(f"Invalid vehicle_type {vehicle_type}")

if __name__ == "__main__":
    v_type = input("Enter vehicle type:\n")
    v_capacity = input("Enter Vehicle capacity:\n")
    vehicle_instance = VehicleFactory.get_instance(v_type)
    vehicle_instance.set_vehicle_capacity(int(v_capacity))
    print(vehicle_instance.get_vehicle_details())