import unittest
import tokenizer


class test_tokenize_line(unittest.TestCase):

    def test_all_words(self):
        line = '/autodily-vlastni/naradi.html'
        tokenized_line = tokenizer.tokenize_line(line)
        for token_group in tokenized_line['tokenized link']:
            for token in token_group:
                assert(token.token_id == tokenizer.TokenId.WORD)

    def test_all_numbers(self):
        line = '/10-234/420'
        tokenized_line = tokenizer.tokenize_line(line)
        for token_group in tokenized_line['tokenized link']:
            for token in token_group:
                assert (token.token_id == tokenizer.TokenId.NUMBER)

    def test_mixed(self):
        line = '/autodily1-mydlo9/'
        tokenized_line = tokenizer.tokenize_line(line)
        for token_group in tokenized_line['tokenized link']:
            for token in token_group:
                assert (token.token_id == tokenizer.TokenId.WORD_WITH_NUMBERS)

class test_detokenize_line(unittest.TestCase):

    def test_detokenize(self):
        line = '/autodily-vlastni/naradi.htm'
        tokens = tokenizer.tokenize_line(line)

        string_to_check = tokenizer.detokenize_line(tokens)

        assert (line == string_to_check)


if __name__ == '__main__':
    unittest.main()
