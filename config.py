import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

VEHICLES_FILE = os.path.join(DATA_DIR, "vehicles.json")
MAINTENANCE_FILE = os.path.join(DATA_DIR, "maintenance.json")

MAINTENANCE_TYPES = [
    "Servicing",
    "Repair",
    "Oil Change",
    "Tyre Change",
    "Insurance",
    "Fuel",
    "Other"
]

STATUSES = ["Pending", "Completed"]
