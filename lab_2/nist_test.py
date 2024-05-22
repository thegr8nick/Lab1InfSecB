import logging
import math
import mpmath

from util import json_loader

logging.basicConfig(level=logging.INFO, filename="tests.txt", filemode='w')

constants = json_loader('constants.json')

MAX_LENGTH_BLOCK = constants["MAX_LENGTH_BLOCK"]
PI = constants["PI"]
SEQUENCE_PATH = constants["SEQUENCE_PATH"]


def frequency_bitwise_test(sequence: str) -> float:
    """
    Perform the frequency bitwise test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:
        x_list = [1 if bit == '1' else -1 for bit in sequence]
        sum_list = sum(x_list)

        s_n = math.fabs(sum_list) / math.sqrt(len(sequence))

        p_value = math.erfc(s_n / math.sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


if __name__ == "__main__":
    sequences = json_loader(SEQUENCE_PATH)
    tests_cpp = sequences["cpp"]
    tests_java = sequences["java"]

    logging.info(f'frequency_bitwise_test for cpp: {frequency_bitwise_test(tests_cpp)}')
    logging.info(f'frequency_bitwise_test for java: {frequency_bitwise_test(tests_java)}')