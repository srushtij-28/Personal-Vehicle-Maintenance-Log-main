from datetime import datetime


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def input_required(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_integer(message, minimum=0):
    while True:
        try:
            value = int(input(message))

            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Enter a valid whole number.")


def input_amount(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Amount cannot be negative.")
                continue

            return round(value, 2)

        except ValueError:
            print("Enter a valid amount.")


def input_date(message):
    while True:
        value = input(message).strip()

        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value

        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def display_vehicle(vehicle):
    print("-" * 60)
    print(f"Vehicle ID    : {vehicle['id']}")
    print(f"Name          : {vehicle['name']}")
    print(f"Vehicle Type  : {vehicle['vehicle_type']}")
    print(f"Registration  : {vehicle['registration']}")
    print(f"Current KM    : {vehicle['odometer']}")


def display_record(record):
    print("-" * 60)
    print(f"Record ID     : {record['id']}")
    print(f"Vehicle       : {record['vehicle_name']}")
    print(f"Type          : {record['maintenance_type']}")
    print(f"Date          : {record['date']}")
    print(f"Odometer      : {record['odometer']} KM")
    print(f"Description   : {record['description']}")
    print(f"Expense       : Rs. {record['expense']:.2f}")
    print(f"Next Due Date : {record['next_due_date'] or 'Not specified'}")
    print(f"Status        : {record['status']}")
