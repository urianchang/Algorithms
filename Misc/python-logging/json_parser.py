import json

with open('test.json') as json_data:
    d = json.load(json_data)
    print(d)
