import json
import requests
from config import BOT_TOKEN


def get_file_id(filename: str) -> str | None:
    try:
        with open('product_instructions/file_id.json', encoding='utf-8') as file:
            files = json.load(file)
            filename = files.get(filename)
            file_id = list(filename.values())[0]
    except (AttributeError, FileNotFoundError):
        file_id = None
    return file_id


def check_file_repository() -> dict:
    try:
        with open('product_instructions/file_id.json', mode="r", encoding='utf-8') as json_file:
            filenames: dict = json.load(json_file)
    except FileNotFoundError:
        """Если файл у нас не существует (удален), создается новый файл"""
        file = open('product_instructions/file_id.json', mode="x", encoding='utf-8')
        file.close()
        filenames = {}
    except json.decoder.JSONDecodeError:
        """Файл создан, но он пуст"""
        filenames = {}
    return filenames


def download_new_document(message, file_info) -> bool:
    req = f'http://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}'
    try:
        with requests.Session() as session:
            """Отправляем запрос на скачивание отправленного файла"""
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
