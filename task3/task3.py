import json
import sys

def get_value(object, id):
    keys = object.keys()
    ret = None

    if 'id' in keys:
        if object.get('id') == id:
            return object.get('value')

    if 'values' in keys:
        for obj in object.get('values'):
            ret = get_value(obj, id)

            if ret != None:
                return ret

def fill_values(object, values):
    keys = object.keys()
    
    if 'value' in keys:
        object.update({'value': get_value(values, object.get('id'))})
            
    if 'values' in keys: 
        for obj in object.get('values'):
            fill_values(obj, values)
    
    if 'tests' in keys:
        for obj in object.get('tests'):
            fill_values(obj, values)

tests = dict()
values = dict()

with open(sys.argv[2], 'r') as file:
    values = json.load(file)

with open(sys.argv[1], 'r') as file:
    tests = json.load(file)

    if type(tests) == type(dict()) and type(values) == type(dict()):
        fill_values(tests, values)

with open('report.json', 'w') as file:
    json.dump(tests, file)