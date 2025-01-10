import json


def read_from_json_as_dictionary(json_path):
    with open(json_path, 'r+') as json_file:
        string_input = json.load(json_file)
    return string_input

def write_from_json_as_dictionary(data, json_path):
    with open(json_path, 'w+') as json_file:
        json.dump(data, json_file, indent=4)

def load_from_json(data):
    return json.dumps(data)

if __name__ == "__main__":
    # dict_to_write = dict()
    # dict_to_write.update(
    #     {"employee_1": {"name": "Dan", "badge_no": 100},
    #      "employee_2": {"name": "Alice", "badge_no": 101}}
    # )
    dict_to_write = [1, 2, "one", "two"]
    write_from_json_as_dictionary(dict_to_write, "data/simple_json.json")
    print(type(read_from_json_as_dictionary("data/simple_json.json")))
    print(type(load_from_json(read_from_json_as_dictionary("data/simple_json.json"))))