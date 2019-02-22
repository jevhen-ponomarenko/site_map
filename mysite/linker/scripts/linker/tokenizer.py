from enum import Enum


class TokenId(Enum):
    WORD = 1
    WORD_WITH_NUMBERS = 2
    NUMBER = 3
    SPECIAL = 4


class Token:

    def __init__(self, token_id, contents, ending):
        self.token_id = token_id
        self.contents = contents
        # this will be populated only if format specifier like .html was  provided
        self.ending = ending

    def __eq__(self, other):
        if (self.token_id == other.token_id) and (self.contents == other.contents):
            return True
        else:
            return False

    def __str__(self):
        if self.ending != '':
            return '{ ' + str(self.token_id) + ' : ' + self.contents + ':' + 'ending is ' + self.ending + '}'
        else:
            return '{ ' + str(self.token_id) + ' : ' + self.contents + '}'

    def __repr__(self):
        return self.__str__()


def tokenize_line(line):
    """ :returns dictionary {"isFolder": bool, "tokenized link": [ [{word}-{word}] / [{word}-{word}] / [{word}-{word}]]}
     """
    link_to_isFolder_dict = {}
    first_tier = []
    list_of_token_groups = line.split('/')
    # remove first element (its an empty string)
    list_of_token_groups.pop(0)
    try:
        if list_of_token_groups[-1] == '\n' or list_of_token_groups[-1] == '':
            # true if link is a folder
            link_to_isFolder_dict["isFolder"] = True
            list_of_token_groups.pop(-1)
    except IndexError:
        print('index error for line: {0}'.format(str(list_of_token_groups)))

    for group in list_of_token_groups:

        second_tier = []
        list_of_possible_tokens = group.split('-')

        for possible_token in list_of_possible_tokens:

            if '\n' in possible_token:
                possible_token = possible_token.replace('\n', '')

            possible_token = remove_file_ending(possible_token);

            if possible_token[0].isalpha():
                token = Token(TokenId.WORD, possible_token[0], possible_token[1])
                second_tier.append(token)

            elif possible_token[0].isnumeric():
                token = Token(TokenId.NUMBER, possible_token[0], possible_token[1])
                second_tier.append(token)

            elif possible_token[0].isalnum():
                token = Token(TokenId.WORD_WITH_NUMBERS, possible_token[0], possible_token[1])
                second_tier.append(token)

            else:
                token = Token(TokenId.SPECIAL, possible_token[0], possible_token[1])
                second_tier.append(token)

        if '.htm' in second_tier[-1].contents:
            second_tier[-1].contents = second_tier[-1].contents.replace('.htm', '')

        first_tier.append(second_tier)

    link_to_isFolder_dict["tokenized link"] = first_tier
    return link_to_isFolder_dict


def remove_file_ending(string_to_check):
    # TODO: fix html and htm
    possible_formats = ('.htm', '.html', '.asp', '.php', '.jsp')

    for ending in possible_formats:
        if ending in string_to_check:
            string_to_check = string_to_check.replace(ending, '')
            return string_to_check, ending

    return string_to_check, ''

def detokenize_line(link_as_tokens):
    """ :param link_as_tokens: array of arrays of tokens see tokenize_line """
    string_to_return = ''

    try:
        for group in link_as_tokens:
            string_to_return += '/'
            number_of_words = len(group)
            for count, token in enumerate(group):
                if count > 0:
                    if count != number_of_words:
                        string_to_return += '-'

                    string_to_return += token.contents
                    string_to_return += token.ending
                else:
                    string_to_return += token.contents
                    string_to_return += token.ending
    # the group is not an array
    except TypeError:
        string_to_return = '/'
        for count, token in enumerate(link_as_tokens):
            number_of_words = len(link_as_tokens)
            if count > 0:
                if count != number_of_words:
                    string_to_return += '-'

                string_to_return += token.contents
                string_to_return += token.ending
            else:
                string_to_return += token.contents
                string_to_return += token.ending

    return string_to_return
