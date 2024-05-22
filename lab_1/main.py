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


def count_frequency(path_input: str) -> dict[str, int]:
    """
    Counting frequency of letters in input file
    :param path_input: str path of file with encrypted text
    :return: dict of frequency letters
    """
    input_string = reader(path_input)
    c = Counter(input_string)
    result = c.most_common()
    return {letter: key / sum(tup[1] for tup in result) for letter, key in result}


def decrypt_text(input_text: str, encrypted_frequency_list: list[str]) -> str:
    """
    Encrypting text using algorithm frequency analysis
    :param input_text: str path of file with encrypted text
    :param encrypted_frequency_list: list of symbols by their frequency in descending order
    :return: str decrypted string
    """
    try:
        arr_encrypt_text = []

        dictionary = dict(zip(encrypted_frequency_list, FREQUENCY_OF_DECRYPTED_TEXT))
        for letter in input_text:
            arr_encrypt_text.append(dictionary[letter])
        text_for_decrypt = ''.join(arr_encrypt_text)
        return text_for_decrypt
    except Exception as e:
        logging.error(f"Error in decryption: {e}\n")


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

    writer(T2_TEXT, decrypt_text(reader(T2_COD3), list(freq[0] for freq in count_frequency(T2_COD3))))
    json_dumper(dict(zip(reader(T2_COD3),
                         decrypt_text(reader(T2_COD3), list(freq[0] for freq in count_frequency(T2_COD3))))), T2_KEY)
    logging.info('Task 2 completed successful')
