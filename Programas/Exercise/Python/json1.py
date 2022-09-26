import json
data = '''{
    "name" : "william",
    "phone" : {
        "type" : "intl",
        "number" : "+57 3218084083"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info =json.loads(data)
print("Name", info["name"])
print("email", info["email"]["hide"])
