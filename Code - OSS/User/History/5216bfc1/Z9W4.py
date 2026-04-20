import json
with open("hello.json", "r") as a:
    data = json.load(a)
print(data)
