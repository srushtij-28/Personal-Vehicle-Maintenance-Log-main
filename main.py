from storage import initialize_storage

from vehicle_manager import (
    add_vehicle,
    view_vehicles
)

from maintenance_manager import (
    add_maintenance_record,
    view_maintenance_records,
    search_maintenance_records,
    view_upcoming_maintenance,
    view_overdue_maintenance
)

from report_manager import show_report


def main():
    initialize_storage()

    while True:
        print("\n========================================")
        print("   PERSONAL VEHICLE MAINTENANCE LOG")
        print("========================================")

        print("1. Register Vehicle")
        print("2. View Vehicles")
        print("3. Add Maintenance Record")
        print("4. View Maintenance History")
        print("5. Search Maintenance Records")
        print("6. View Upcoming Maintenance")
        print("7. View Overdue Maintenance")
        print("8. View Expense Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_vehicle()

        elif choice == "2":
            view_vehicles()

        elif choice == "3":
            add_maintenance_record()

        elif choice == "4":
            view_maintenance_records()

        elif choice == "5":
            search_maintenance_records()

        elif choice == "6":
            view_upcoming_maintenance()

        elif choice == "7":
            view_overdue_maintenance()

        elif choice == "8":
            show_report()

        elif choice == "9":
            print("\nThank you for using the maintenance log!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
