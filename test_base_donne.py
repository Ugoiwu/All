import json

with open('myDictionary.json') as json_file:
    usernames = json.load(json_file)


def new_user(username, age):
    id = len(usernames) + 1
    existing_usernames = []
    for key in usernames:
        existing_usernames.append(usernames[key]["username"])
    while username in existing_usernames:
        username = input('Username already existing, please try again: ')
        
    usernames[id] = {"username": username, "age": age}
        
new_user(input('Username ? '), input('Age ? '))
with open("myDictionary.json", "w") as tf:
    json.dump(usernames,tf)