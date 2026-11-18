import json

activity = {
    "application": "LogStream",
    "date": "2026-11-18",
    "total_requests": 150,
    "errors": 12,
    "warnings": 8,
    "users": [
        {"id": 1, "action": "login"},
        {"id": 2, "action": "logout"},
        {"id": 3, "action": "login"}
    ]
}


if __name__ == '__main__':
    # json.dumps() convert dict to json string
    json_stirng = json.dumps(activity, indent=4)
    # print(json_stirng)
    # print(type(json_stirng))


    with open('activity.json', 'w')as file:
        # json.dump() save py dict in file as json
        json.dump(activity, file, indent=4)

    # json.load() read json file and convert it to py dict
    with open('activity.json', 'r') as file:
        loaded_json = json.load(file)
    # print(loaded_json["application"])
    # print(loaded_json["errors"])

    incoming_data = '''
{
    "user_id": 25,
    "action": "login",
    "status": "success"
}
'''
    # json.loads() Imagine another backend service sends you this JSON String
    parsed_data = json.loads(incoming_data)
    print(parsed_data['user_id'])
