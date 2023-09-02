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

input_json = json.loads(input_json1)
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
    # print(message[bus_id], message[a_time])
    bus_stops.setdefault(message[bus_id], dict())
    bus_stops[message[bus_id]][message[stop_name]] = message[a_time]

# print(bus_stops)

errors_found = False

for bus, stops in bus_stops.items():
    print(stops)
    # for i in range(0, len(stops)):
    #     stops_iterator = iter(stops)
    #     if i == len(stops) - 1:
    #         break
    #     time_parsed_previous = stops[bus_stops_keys[i]].split(":")
    #     # print(time_parsed_previous)
    #     time_parsed_next = stops[bus_stops_keys[i + 1]].split(":")

    #     # hours of the previous more or equal next
    #     if time_parsed_previous[0] >= time_parsed_next[0]:
    #         # minutes of the previous more or equal next
    #         if time_parsed_previous[1] >= time_parsed_next[1]:
    #             # clean up not necessary stops info
    #             bus_stops[bus].clear()
    #             # save bus station to the bus line as False
    #             bus_stops[bus][bus_stops_keys[i + 1]] = False
                
    #             # update errors_found
    #             errors_found = True
                
    #             # exit the current bus line loop
    #             break

# for bus, stops in bus_stops.items():
#     bus_stops_keys = list(stops.keys())
#     # print("bus_stops_keys", bus_stops_keys)
#     for i in range(0, len(stops)):
#         stops_iterator = iter(stops)
#         if i == len(stops) - 1:
#             break
#         time_parsed_previous = stops[bus_stops_keys[i]].split(":")
#         # print(time_parsed_previous)
#         time_parsed_next = stops[bus_stops_keys[i + 1]].split(":")

#         # hours of the previous more or equal next
#         if time_parsed_previous[0] >= time_parsed_next[0]:
#             # minutes of the previous more or equal next
#             if time_parsed_previous[1] >= time_parsed_next[1]:
#                 # clean up not necessary stops info
#                 bus_stops[bus].clear()
#                 # save bus station to the bus line as False
#                 bus_stops[bus][bus_stops_keys[i + 1]] = False
                
#                 # update errors_found
#                 errors_found = True
                
#                 # exit the current bus line loop
#                 break

# print(bus_stops)


# output
# Arrival time test:
# bus_id line 128: wrong time on station Fifth Avenue
# bus_id line 256: wrong time on station Sunset Boulevard

if errors_found:
    print("Arrival time test:")
    for bus_id, stops in bus_stops.items():
        if len(stops) > 1:
            continue
        print(f"bus_id line {bus_id}: wrong time on station {list(stops.keys())[0]}")
else:
    print("Arrival time test:")
    print("OK")