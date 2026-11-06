from storage import load_vehicles, save_vehicles
from utils import (
    get_next_id,
    input_required,
    input_integer,
    display_vehicle
)


def add_vehicle():
    vehicles = load_vehicles()

    print("\n--- REGISTER VEHICLE ---")

    name = input_required("Enter vehicle name: ")
    vehicle_type = input_required("Enter vehicle type: ")
    registration = input_required("Enter registration number: ").upper()

    if any(
        vehicle["registration"].lower() == registration.lower()
        for vehicle in vehicles
    ):
        print("This registration number is already registered.")
        return

    odometer = input_integer("Enter current odometer reading (KM): ")

    vehicle = {
        "id": get_next_id(vehicles),
        "name": name,
        "vehicle_type": vehicle_type,
        "registration": registration,
        "odometer": odometer
    }

    vehicles.append(vehicle)
    save_vehicles(vehicles)

    print("\nVehicle registered successfully!")


def view_vehicles():
    vehicles = load_vehicles()

    if not vehicles:
        print("\nNo vehicles registered.")
        return

    print("\n--- REGISTERED VEHICLES ---")

    for vehicle in vehicles:
        display_vehicle(vehicle)


def select_vehicle():
    vehicles = load_vehicles()

    if not vehicles:
        print("Please register a vehicle first.")
        return None

    print("\n--- SELECT VEHICLE ---")

    for vehicle in vehicles:
        print(
            f"{vehicle['id']}. {vehicle['name']} "
            f"({vehicle['registration']})"
        )

    try:
        vehicle_id = int(input("Enter vehicle ID: "))
    except ValueError:
        print("Enter a valid vehicle ID.")
        return None

    vehicle = next(
        (item for item in vehicles if item["id"] == vehicle_id),
        None
    )

    if not vehicle:
        print("Vehicle not found.")
        return None

    return vehicle
