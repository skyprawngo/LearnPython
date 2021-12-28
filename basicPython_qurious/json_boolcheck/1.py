import os
import json

def import_json():
    cwd_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"switch.json"))
    with open(cwd_path, "r", encoding = 'utf-8') as reader:
        switch = json.loads(reader.read())
    return switch
    
a = import_json()
print(type(a["check_bool"]))
print(type(a["check_int"]))
