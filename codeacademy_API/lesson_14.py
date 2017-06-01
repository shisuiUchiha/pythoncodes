import json
from pprint import pprint

f = open('pets_json.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)