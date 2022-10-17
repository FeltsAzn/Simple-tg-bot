import json


def get_file_id(filename):
    with open('product_instructions/file_id.json', encoding='utf-8') as file:
        files = json.load(file)
        file_id = list(files[filename].values())[0]
    return file_id


print(get_file_id(filename="filename_1"))