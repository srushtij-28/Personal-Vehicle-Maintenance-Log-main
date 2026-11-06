import json
import os

from config import DATA_DIR, VEHICLES_FILE, MAINTENANCE_FILE


def initialize_storage():
    os.makedirs(DATA_DIR, exist_ok=True)

    for file_path in [VEHICLES_FILE, MAINTENANCE_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file, indent=4)


def load_json(file_path):
    initialize_storage()

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_json(file_path, data):
    initialize_storage()

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_vehicles():
    return load_json(VEHICLES_FILE)


def save_vehicles(vehicles):
    save_json(VEHICLES_FILE, vehicles)


def load_maintenance():
    return load_json(MAINTENANCE_FILE)


def save_maintenance(records):
    save_json(MAINTENANCE_FILE, records)
