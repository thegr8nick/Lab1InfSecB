import json
import logging

logging.basicConfig(level=logging.INFO)


def json_loader(file_name: str) -> dict:
    """
    Reading json file in dict
    :param file_name: path to json file
    :return: dict result
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f'File was not found: {e}')