import json

python_obj = {
    "ten": "Bui Duc Hiep",
    "tuoi": 19,
    "thanh_pho": "Ha Noi"
}

json_data = json.dumps(python_obj, indent=4, sort_keys=True)

print("Chuỗi JSON (sắp xếp theo khóa, thụt lề 4):\n", json_data)