import qrcode
from datetime import datetime
import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def generate_qrcode(vehicle_id, json_file):
    entry_time = datetime.now()
    data = f"{vehicle_id},{entry_time.strftime('%Y-%m-%d %H:%M:%S')}"
    qr = qrcode.make(data)
    qr.save(f"{vehicle_id}_entry.png")
    print(f"QR Code untuk kendaraan {vehicle_id} dibuat dengan waktu masuk {entry_time}")

    
    json_data = read_json(json_file)

    json_data[vehicle_id] = {
        "entry_time": entry_time.strftime('%Y-%m-%d %H:%M:%S'),
        "file_name": f"{vehicle_id}_entry.png"
    }

    write_json(json_data, json_file)

vehicle_id = "Jazz"
json_file = "database.json"
generate_qrcode(vehicle_id, json_file)
