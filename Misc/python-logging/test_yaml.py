import yaml

with open('logging.yaml', 'r') as f:
    config = yaml.load(f)
    print config["formatters"]
    for f in config["formatters"]:
        # print "**", f
        config["formatters"][f] = {"()": "TESTER"}
    # config["formatters"] = "hi"
    print config["formatters"]
