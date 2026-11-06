from datetime import date

from config import MAINTENANCE_TYPES
from storage import (
    load_vehicles,
    save_vehicles,
    load_maintenance,
    save_maintenance
)

from vehicle_manager import select_vehicle

from utils import (
    get_next_id,
    input_required,
    input_integer,
    input_amount,
    input_date,
    display_record
)


def add_maintenance_record():
    vehicle = select_vehicle()

    if vehicle is None:
        return

    print("\n--- MAINTENANCE TYPES ---")

    for index, maintenance_type in enumerate(
        MAINTENANCE_TYPES, start=1
    ):
        print(f"{index}. {maintenance_type}")

    try:
        choice = int(input("Select maintenance type: "))
    except ValueError:
        print("Enter a valid choice.")
        return

    if choice < 1 or choice > len(MAINTENANCE_TYPES):
        print("Invalid maintenance type.")
        return

    maintenance_type = MAINTENANCE_TYPES[choice - 1]

    maintenance_date = input_date(
        "Enter maintenance date (YYYY-MM-DD): "
    )

    odometer = input_integer(
        "Enter odometer reading (KM): "
    )

    if odometer < vehicle["odometer"]:
        print("Odometer reading cannot be lower than the vehicle's current reading.")
        return

    description = input_required("Enter maintenance description: ")
    expense = input_amount("Enter expense (Rs.): ")

    next_due_date = input(
        "Enter next due date (YYYY-MM-DD) or leave blank: "
    ).strip()

    if next_due_date:
        try:
            date.fromisoformat(next_due_date)
        except ValueError:
            print("Invalid date format.")
            return

    records = load_maintenance()

    record = {
        "id": get_next_id(records),
        "vehicle_id": vehicle["id"],
        "vehicle_name": vehicle["name"],
        "registration": vehicle["registration"],
        "maintenance_type": maintenance_type,
        "date": maintenance_date,
        "odometer": odometer,
        "description": description,
        "expense": expense,
        "next_due_date": next_due_date or None,
        "status": "Completed"
    }

    records.append(record)

    vehicle_records = load_vehicles()

    for item in vehicle_records:
        if item["id"] == vehicle["id"]:
            item["odometer"] = max(item["odometer"], odometer)

    save_maintenance(records)
    save_vehicles(vehicle_records)

    print("\nMaintenance record added successfully!")


def view_maintenance_records():
    records = load_maintenance()

    if not records:
        print("\nNo maintenance records found.")
        return

    print("\n--- MAINTENANCE HISTORY ---")

    for record in records:
        display_record(record)


def search_maintenance_records():
    records = load_maintenance()

    keyword = input_required(
        "Enter vehicle name or registration number: "
    ).lower()

    results = [
        record for record in records
        if keyword in record["vehicle_name"].lower()
        or keyword in record["registration"].lower()
    ]

    if not results:
        print("\nNo matching records found.")
        return

    print("\n--- SEARCH RESULTS ---")

    for record in results:
        display_record(record)


def view_upcoming_maintenance():
    records = load_maintenance()
    today = date.today()

    upcoming = [
        record for record in records
        if record["next_due_date"]
        and date.fromisoformat(record["next_due_date"]) >= today
    ]

    if not upcoming:
        print("\nNo upcoming maintenance records.")
        return

    print("\n--- UPCOMING MAINTENANCE ---")

    for record in upcoming:
        display_record(record)


def view_overdue_maintenance():
    records = load_maintenance()
    today = date.today()

    overdue = [
        record for record in records
        if record["next_due_date"]
        and date.fromisoformat(record["next_due_date"]) < today
    ]

    if not overdue:
        print("\nNo overdue maintenance records.")
        return

    print("\n--- OVERDUE MAINTENANCE ---")

    for record in overdue:
        display_record(record)
