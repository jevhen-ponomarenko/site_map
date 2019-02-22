import os
from .tokenizer import tokenize_line


def parse_file(path):
    """:returns dictionary {0 : dict, 1 : dict, ...}"""
    print('parsing file {0}'.format(path))
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


def load_file_as_array_of_pairs(path):
    print('loading file {0}'.format(path))
    lines = []
    file = open(path, 'r')
    first = True
    for line in file:
        if first == False:
            two_links = line.split(';')
            tuple_ret = (two_links[0],two_links[1])
            lines.append(tuple_ret)
        first = False
    file.close()
    return lines

