import json

json_data = '{"ten": "Bui Duc Hiep", "tuoi": 19, "thanh_pho": "Ha Noi"}'

python_obj = json.loads(json_data)

print("Đối tượng Python:", python_obj)