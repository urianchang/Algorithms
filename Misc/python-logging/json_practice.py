import json

# log_obj = json.dumps({"1": 1})
log_obj = {"1": 1}

# Edit JSON file
with open('test.json', 'r+') as json_file:
        d = json.load(json_file)
        d['logs'].append(log_obj)
        json_file.seek(0)
        json.dump(d, json_file, indent=4)
        json_file.truncate()
