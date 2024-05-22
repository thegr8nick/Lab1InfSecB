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


def consecutive_bits_test(sequence: str) -> float:
    """
    Perform the same consecutive bits test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:
        sum_list = sequence.count("1") / len(sequence)
        if abs(sum_list - 0.5) >= (2 / math.sqrt(len(sequence))):
            return 0

        v_n = 0
        v_n += sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(len(sequence) - 1))

        p_value = math.erfc(abs(v_n - 2 * len(sequence) * sum_list * (1 - sum_list)) / (
                2 * math.sqrt(2 * len(sequence)) * sum_list * (1 - sum_list)))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


if __name__ == "__main__":
    sequences = json_loader(SEQUENCE_PATH)
    tests_cpp = sequences["cpp"]
    tests_java = sequences["java"]

    logging.info(f'frequency_bitwise_test for cpp: {frequency_bitwise_test(tests_cpp)}')
    logging.info(f'consecutive_bits_test for cpp: {consecutive_bits_test(tests_cpp)}')
    logging.info(f'frequency_bitwise_test for java: {frequency_bitwise_test(tests_java)}')
    logging.info(f'consecutive_bits_test for java: {consecutive_bits_test(tests_java)}')