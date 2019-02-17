import unittest
import os
from parser import parse_file
from tokenizer import TokenId

class test_parse_file(unittest.TestCase):

    PATH_TO_DATA = '../data/test_data.csv'

    def test_parse_file_positive(self):
        parsed_file = parse_file(self.PATH_TO_DATA)
        # dictionary is not empty
        assert (len(list(parsed_file)) > 0)
        array_2d = parsed_file[0]['tokenized link']

        assert (len(array_2d) == 2)
        # see data file
        assert (array_2d[0][0].token_id == TokenId.WORD_WITH_NUMBERS and array_2d[0][0].contents == '1st')





