import json
import aiohttp
import requests
from config import BOT_TOKEN
import aiofiles


def get_file_id(filename):
    try:
        with open('product_instructions/file_id.json', encoding='utf-8') as file:
            files = json.load(file)
            filename = files.get(filename)
            file_id = list(filename.values())[0]
    except (AttributeError, FileNotFoundError):
        file_id = None
    return file_id


def download_new_document(message, file_info):
    req = f'http://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}'
    try:
        with requests.Session() as session:
            response = session.get(req)
            downloaded_file = response.content
            with open(f'product_instructions/{message.document.file_name}', 'w+b') as file:
                file.write(downloaded_file)
        try:
            with open('product_instructions/file_id.json', 'r', encoding='utf-8') as file:
                filenames = json.load(file)
        except json.decoder.JSONDecodeError:
            filenames = {}
        with open('product_instructions/file_id.json', 'w', encoding='utf-8') as file:
            filenames[f"filename_{len(filenames) + 1}"] = {message.document.file_name: file_info.file_id}
            json.dump(filenames, file, indent=4)

    except Exception:
        return False
    return True
