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

def register_user(slots):
    name = input("👤 Ismingiz: ").strip()
    if is_already_registered(slots, name):
        print("❌ Siz allaqachon ro‘yxatdan o‘tgansiz.")
        return
    
    while True:
        show_available_slots(slots)
        choice = input("🕒 Vaqt oralig'ini tanlang (masalan: 12:00–12:30): ").strip()
        if choice not in slots:
            print("⚠️ Bunday vaqt oralig‘i mavjud emas. Qayta urinib ko‘ring.")
            continue
        if len(slots[choice]) >= LIMIT:
            print("⛔️ Bu vaqt to‘la. Iltimos boshqa vaqt tanlang.")
            continue
        slots[choice].append(name)
        save_slots(slots)
        print(f"✅ {name}, siz {choice} vaqt oralig‘iga muvaffaqiyatli ro‘yxatdan o‘tdingiz.")
        break