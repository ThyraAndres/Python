import json
data = '''[
    {"id" : "1005281509",
    "x" : "22",
    "name" : "William"
    },
    {
    "id" : "1005281508",
    "x" : "21",
    "name" : "William"
    }
]'''

info = json.loads(data)
print('User count:', len(info))
for item in info:
    print("ID", item["id"])
    print("X", item["x"])
    print("Name", item["name"])
