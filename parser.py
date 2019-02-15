import os
from tokenizer import tokenize_line


def parse_file(path):
    """:returns dictionary {0 : dict, 1 : dict, ...}"""
    counter = 0
    line_num_to_tokens_dict = {}

    try:
        file = open(path, 'r')
        for line in file:
            if (line == ''):
                break

            line_num_to_tokens_dict[counter] = tokenize_line(line)
            counter += 1
        file.close()
        return line_num_to_tokens_dict

    except FileNotFoundError:
        print('{0} File not Found'.format(path))




