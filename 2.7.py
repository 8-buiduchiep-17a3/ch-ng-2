import json

python_obj = {
    "ten": "Bui Duc Hiep",
    "tuoi": 19,
    "thanh_pho": "Ha Noi"
}

json_data = json.dumps(python_obj)

print("Chuỗi JSON:", json_data)