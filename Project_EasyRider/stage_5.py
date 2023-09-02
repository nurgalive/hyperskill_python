import json

input_json1 = """[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
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
        "a_time": "08:17"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:07"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
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
        "a_time": "09:44"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
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
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]"""

input_json2 = """[{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]"""

input_json = json.loads(input_json2)
# input_json = json.loads(input())

a_time = "a_time"
bus_id = "bus_id"
stop_name = "stop_name"

bus_stops = {}  # {256: {"Bourbon Street": "08:13", "Sunset Boulevard": "08:16", ...},
#  512: {...},
# }
# {
#     128: {'Prospekt Avenue': '08: 12', 'Elm Street': '08: 19', 'Fifth Avenue': '08: 17', 'Sesame Street': '08: 07'
#     },
#     256: {'Pilotow Street': '09: 20', 'Elm Street': '09: 45', 'Sunset Boulevard': '09: 44', 'Sesame Street': '10: 12'
#     },
#     512: {'Bourbon Street': '08: 13', 'Sunset Boulevard': '08: 16'
#     }
# }

for message in input_json:
    # print(message[bus_id], message)
    bus_stops.setdefault(message[bus_id], [])
    bus_stops[message[bus_id]].append(message)

# print(bus_stops)

errors_found = False

for bus, values in bus_stops.items():
    # print(bus, values)
    a_time = values[0]["a_time"]
    for value in values[1:]:
        if a_time > value["a_time"]:
            print(f"bus_id line {bus}: wrong time on station {value['stop_name']}")
            errors_found = True
            break
        a_time = value["a_time"]

if not errors_found:
    print("Arrival time test:")
    print("OK")