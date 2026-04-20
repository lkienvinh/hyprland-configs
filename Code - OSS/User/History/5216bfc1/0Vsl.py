a = {}

a = {"name": 123,
     "age": 10,
     "sex": "male"}
print(a["name"])

import json
with open ("hello.json", "r") as a:
    data = json.load(a)
    print(data)