
import json
import os

DB_FILE = "groups.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_group(chat_id, title):
    data = load_data()

    if str(chat_id) not in data:
        data[str(chat_id)] = {
            "title": title
        }

    save_data(data)

def get_groups():
    return load_data()
