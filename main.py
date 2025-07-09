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

def save_slots(slots):
    with open(FILENAME, "w") as file:
        json.dump(slots, file, indent=4)

def show_available_slots(slots):
    print("\n📅 Bo'sh vaqt oralig'lari:")
    for time, people in slots.items():
        free = LIMIT - len(people)
        status = f"{free} o‘rin bo‘sh" if free > 0 else "To‘la"
        print(f"{time} - {status}")

def is_already_registered(slots, name):
    for people in slots.values():
        if name in people:
            return True
    return False