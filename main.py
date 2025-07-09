import json
import os

FILENAME = "registrations.json"
LIMIT = 5

default_slots = {
    "12:00 - 12:30": [],
    "12:30 - 13:00": [],
    "13:00 - 13:30": []
}

def load_slots():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return default_slots.copy()