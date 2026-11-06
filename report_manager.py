from storage import load_vehicles, load_maintenance


def show_report():
    vehicles = load_vehicles()
    records = load_maintenance()

    total_vehicles = len(vehicles)
    total_records = len(records)

    total_expense = sum(
        record["expense"] for record in records
    )

    maintenance_counts = {}

    for record in records:
        maintenance_type = record["maintenance_type"]

        maintenance_counts[maintenance_type] = (
            maintenance_counts.get(maintenance_type, 0) + 1
        )

    print("\n========== VEHICLE MAINTENANCE REPORT ==========")
    print(f"Total Vehicles       : {total_vehicles}")
    print(f"Maintenance Records  : {total_records}")
    print(f"Total Expenses       : Rs. {total_expense:.2f}")

    print("\nMaintenance by Type:")

    if not maintenance_counts:
        print("No maintenance records available.")
    else:
        for maintenance_type, count in maintenance_counts.items():
            print(f"{maintenance_type:<20}: {count}")

    print("================================================")
