import json

input_json1 = json.loads(input())

bus_id = "bus_id"
stop_name = "stop_name"
output_json = {}

for message in input_json1:
        if message[bus_id] not in output_json:
            output_json[message[bus_id]] = set()
        output_json[message[bus_id]].add(message[stop_name])

print("Line names and number of stops:")
print(f"\n".join(f"bus_id: {key}, stops: {len(value)}" for key, value in output_json.items()))