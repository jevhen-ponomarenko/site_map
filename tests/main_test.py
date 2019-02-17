import unittest
from parser import parse_file
from parser import load_file_as_array_of_pairs
import tokenizer
import compare

class testTwoFiles(unittest.TestCase):
    def test_protruck(self):
        old_links = parse_file('../data/old.csv')
        new_links = parse_file('../data/new.csv')
        good = 0
        bad = 0
        actual_data = load_file_as_array_of_pairs('../data/URL_protruck.csv')

        candidates = compare.find_candidates_for_file(new_links, old_links)

        for pair in candidates:
            orig_link = tokenizer.detokenize_line(pair[0]['tokenized link'])

            for line in actual_data:
                if orig_link == line[1]:
                    for link in pair[1]:
                        if link + '/' == line[0]:
                            good += 1


        assert (good > 0)