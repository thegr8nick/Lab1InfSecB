import argparse
import logging

from two_type_operations import TwoTypeOperations
from symmetric import Symmetric
from asymmetric import Asymmetric
from utility import UtilityWorkFile
from constants import PATHS_DEFAULT


def main():
    parser = argparse.ArgumentParser(description="Entry point of the program")
    paths_default = UtilityWorkFile(PATHS_DEFAULT)
    paths_dict = paths_default.read_json_file()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-key', '--keys',
                       action='store_true',
                       help='Run key generation mode.')
    group.add_argument('-enc', '--encryption',
                       action='store_true',
                       help='Run encryption mode.')
    group.add_argument('-dec', '--decryption',
                       action='store_true',
                       help='Run decryption mode.')

    parser.add_argument('-k', '--key_length',
                        type=int,
                        default=64,
                        help='Length of the symmetric key in bits (default: 448).')

    parser.add_argument('-text', '--input_text_file',
                        type=str,
                        default=paths_dict["text_file"],
                        help='Path of the input txt file with text(default: paths_dict["text_file"]')

    parser.add_argument('-public_key', '--public_key_path',
                        type=str,
                        default=paths_dict["public_key"],
                        help='Path of the public pem file with key(default: paths_dict["public_key"]')

    parser.add_argument('-private_key', '--private_key_path',
                        type=str,
                        default=paths_dict["private_key"],
                        help='Path of the private pem file with key(default: paths_dict["private_key"]')

    parser.add_argument('-sym_key', '--symmetric_key_path',
                        type=str,
                        default=paths_dict["symmetric_key_file"],
                        help='Path of the symmetric txt file with key(default: paths_dict["symmetric_key_file"]')

    parser.add_argument('-enc_path', '--encrypted_text_path',
                        type=str,
                        default=paths_dict["encrypted_text_file"],
                        help='Path of the txt file with encrypted text(default: paths_dict["encrypted_text_file"]')

    parser.add_argument('-dec_path', '--decrypted_text_path',
                        type=str,
                        default=paths_dict["decrypted_text_file"],
                        help='Path of the txt file with decrypted text(default: paths_dict["decrypted_text_file"]')

    try:
        args = parser.parse_args()
        if args.key_length != 64 and args.key_length != 128 and args.key_length != 192:
            raise argparse.ArgumentTypeError
        symmetric_crypto = Symmetric(args.key_length)
        asymmetric_crypto = Asymmetric(args.private_key_path, args.public_key_path)
        two_type_operate = TwoTypeOperations(args.input_text_file,
                                             args.symmetric_key_path, args.encrypted_text_path,
                                             args.decrypted_text_path, symmetric_crypto, asymmetric_crypto)
        match args:
            case args if args.keys:
                two_type_operate.generate_keys()

            case args if args.encryption:
                two_type_operate.encrypt_text()

            case args if args.decryption:
                two_type_operate.decrypt_text()

    except argparse.ArgumentTypeError:
        logging.error(f"Error in arguments, key_length must be in 64, 128 or 192 bits")


if __name__ == "__main__":
    main()
