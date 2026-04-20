import json
with open("hello.json", "r") as a: # Đổi "w" thành "r"
    data = json.load(a)
