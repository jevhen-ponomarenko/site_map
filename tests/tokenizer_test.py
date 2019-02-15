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


if __name__ == '__main__':
    unittest.main()
