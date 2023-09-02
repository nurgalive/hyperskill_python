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
        "stop_type": "O",
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
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
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
        "stop_type": "O",
        "a_time": "09:59"
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

input_json2 = """[
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

input_json = json.loads(input_json2)

# print(input_json)

# Check that all the departure points, final stops, and transfer stations are not "On-demand".

# 1. Create a list of of finat stops, depature stops and transfer stops.
# 2. Create a list of on-demand stops.
# 3. Check that on-demand stops are not presented in the list of stops, if yes, save these stops.

all_stops = []
finish_start_transfer_stops = []
on_demands_stops = []
error_stops = set()
stop_type = {"S", "F"}
error_stops = []


stop_name = "stop_name"
stop_type = "stop_type"


for message in input_json:
    # print(message)

    # collecting finish and start stops
    if message[stop_type] in stop_type:
        finish_start_transfer_stops.append(message[stop_name])
    
    # collection on demand stops
    if message[stop_type] == "O":
        on_demands_stops.append(message[stop_name])

    # collecting all stops for getting transfer stops
    all_stops.append(message[stop_name])


# getting transfer stops
for stop in set(all_stops):
    if all_stops.count((stop)) > 1:
        finish_start_transfer_stops.append(stop)

# checking on-demand stops with all stops
for stop in on_demands_stops:
    if stop in finish_start_transfer_stops:
        error_stops.append(stop)

if error_stops:
    print("On demand stops test:")
    print(f"Wrong stop type: {sorted(error_stops)}")
else:
    print("On demand stops test:")
    print("OK")