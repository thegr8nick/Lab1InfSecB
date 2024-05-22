import logging
import sys

from collections import Counter

from functions_helpers import json_loader, reader, writer, json_dumper

logging.basicConfig(level=logging.INFO)

SHIFT = int(sys.argv[1])

constants = json_loader('constants.json')

ALPHABET = constants["ALPHABET"]
PATHS = constants["PATHS"]
FREQUENCY_OF_DECRYPTED_TEXT = constants["FREQUENCY_OF_DECRYPTED_TEXT"]

def caesar_cipher(path_input: str, shift_number: int) -> str:
    """Encrypting text using caesar cipher with shift
    :param path_input: str path of the input string
    :param shift_number: int number of shift
    :return: str encrypted string
    """
    encrypted = ""

    input_text = reader(path_input)

    for letter in input_text:
        if letter in ALPHABET:
            new_code = (ALPHABET[letter] + shift_number) % len(ALPHABET)
            encrypted_letter = next(
                symbol
                for symbol, code in ALPHABET.items()
                if code == new_code
            )
            encrypted += encrypted_letter
        else:
            encrypted += letter
    return encrypted

if __name__ == '__main__':
    paths_dict = json_loader(PATHS)

    T1_TEXT = paths_dict['t1_text']
    T1_TEXT_CODE = paths_dict['t1_text_code']
    T1_KEY = paths_dict["t1_key"]
    T2_COD3 = paths_dict['t2_cod3']
    T2_KEY = paths_dict['t2_key']
    T2_TEXT = paths_dict['t2_text']

    writer(T1_TEXT_CODE, caesar_cipher(T1_TEXT, SHIFT))
    json_dumper(dict(zip(reader(T1_TEXT), caesar_cipher(T1_TEXT, SHIFT))), T1_KEY)
    logging.info('Task 1 completed successful')