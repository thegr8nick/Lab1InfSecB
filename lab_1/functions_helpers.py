import json
import logging

logging.basicConfig(level=logging.INFO)


def reader(file_name: str) -> str:
    """
    Reading txt file in string
    :param file_name: path to txt file
    :return: str result string
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return ''.join(file.readlines())
    except Exception as e:
        logging.error(f'File was not found: {e}')


def writer(file: str, data: str) -> None:
    """Writing to txt file input string
    :param file: str path to txt file
    :param data: str input string
    :return:
    """
    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        logging.error(f'File was not found: {e}')


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


def json_dumper(data: dict, file_name: str) -> None:
    """Writing to json file input string
    :param file_name: str path to json file
    :param data: dict input dict
    :return:
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
    except Exception as e:
        logging.error(f'File was not found: {e}')
