import json

bus_dict = [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]

bus_dict_test = [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": 3,
        "a_time": "8.12"
    }
    ]

def check_required_field(key: str, dict_to_check: dict) -> bool:
    if len(str(dict_to_check[key])) > 0 or key == "stop_type":
        return True
    else:
        return False

def check_field_type(key: str, value) -> bool:
    field_types_dict = {
    "bus_id": int,
    "stop_id": int,
    "stop_name": str,
    "next_stop": int,
    "a_time": str
    }

    special_field_type_dict = {
    "stop_type": str
    }

    if key in field_types_dict:
        if isinstance(value, field_types_dict[key]):
            return True
        else:
            return False
    elif key in special_field_type_dict:
        if len(str(value)) == 0:
            return True
        else:
            if isinstance(value, special_field_type_dict[key]) and \
                    len(str(value)) == 1:
                return True
            else:
                False


input_json = json.dumps(bus_dict_test)
# print(input_json)

input_json1 = json.loads(input_json)

output_json = {
    "bus_id": 0,
    "stop_id": 0,
    "stop_name": 0,
    "next_stop": 0,
    "stop_type": 0,
    "a_time": 0,
}

for message in input_json1:
    # print(i)
    for key, value in message.items():
        # print(key)

        # check that we are testing not a random key
        if key in output_json.keys():
            # check that field in not empty
            if check_required_field(key, message):
                # check the field value type
                if not check_field_type(key, value):
                    output_json[key] += 1
            else:
                output_json[key] += 1


# result
num_of_errors = 0
for val in output_json.values():
    num_of_errors += val
print(f"Type and required field validation: {num_of_errors} errors")
for key, value in output_json.items():
    print(f"{key}: {value}")