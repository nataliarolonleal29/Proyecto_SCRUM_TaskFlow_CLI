import json

FILE = "data.json"

def load_data():
    with open(FILE, "r") as file:
        return json.load(file)
    
def save_data (data):
    with open(FILE, "w") as file:
        return json.dump(data, file, indent=4)