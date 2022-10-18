import json


def get_file_id(filename):
    with open('../product_instructions/file_id.json', encoding='utf-8') as file:
        files = json.load(file)
        try:
            file_id = list(files.get(filename).values())[0]
        except AttributeError:
            file_id = None
    return file_id
