import json, pprint

#A1
path = "m_pprint.json"
with open(path, "r") as file:
    data = json.load(file)

#A2
pprint.pp(data)

#A3
pp = pprint.PrettyPrinter(indent= 4, depth = 2, sort_dicts = False)

#A4
pp.pprint(data[1])
pp.pprint(data[3])
