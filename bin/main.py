import argparse
import os
import re

from collections import Counter
from time import sleep

def main():
    args = _build_parser()

    print("Counting Letters...")
    sleep(1)

    textfile = Book(args.filename)
    main_return = textfile.count_letters()
    letter_count, title, total_num = main_return[0], main_return[1], main_return[2]

    print("Calculating Frequencies in Decimal...")
    sleep(1)

    frequency = _probability(letter_count, total_num)

    print("Writing to file...")
    sleep(1)

    _write_file(frequency, title)
    print(f"Program End. See 'Frequencies.txt' to see letter frequencies for {title}")

def _probability(letter_counter, total_num):
    frequencies = {char: round(num/total_num, 4) for char, num in letter_counter.items()}
    sorted_frequencies = {key: value for key, value in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
    return sorted_frequencies

def _write_file(frequencies, title):
    with open("Frequencies.txt", 'a') as file:
        file.write(f"Title of book is: {title}\n\n")
        for item in frequencies.items():
            file.write(f"{item}\n")


def _build_parser():
    """ Build Parser to accept user-defined argument """
    parser = argparse.ArgumentParser(description="Letter Frequency Calculator")
    required_args = parser.add_argument_group('Required Arguments')
    required_args.add_argument('-f', '--filename', required=True, type=_check_file, help="Please enter the relative or "
                                                                                         "absolute path of the textfile "
                                                                                         "to be examined")
    args = parser.parse_args()
    print(f"Parameters Inputted: Text file = {args.filename}")
    return args


def _check_file(textfile):
    if not os.path.isfile(textfile):
        raise argparse.ArgumentTypeError(f"File path of {textfile} cannot be found, or is not a file. "
                                         f"Please check the file path")
    try:
        with open(textfile, 'r', encoding='utf8') as file:
            file.read()
            return textfile
    except IOError:
        raise argparse.ArgumentTypeError(f"{textfile} was found, but the file is not readable. Check permissions")


class Book:

    def __init__(self, textfile):
        self.textfile = textfile

    def count_letters(self):
        with open(self.textfile, 'r', encoding='utf8') as file:
            full_text = file.read()
            title = self.get_title(full_text)

            counter = Counter(char for char in full_text.lower() if char.isalpha() and char.isascii())
            total_num = sum(counter.values())

            return counter, title, total_num

    @staticmethod
    def get_title(textfile):
        regex = re.compile(r'Title:\s(.*)')
        title = regex.search(textfile).group(1)
        return title


if __name__ == '__main__':
    main()
