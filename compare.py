from parser import parse_file
import time
"""
:returns array of arrays of tokens 
finds nearest possible candidates for the provided link in the file
    

"""

def find_candidates_for_line(file_as_dict, link_as_tokens):
    dict_to_return = {}
    possible_candidates = []
    for link_data in file_as_dict.values():

        num_of_same_tokens = 0
        # nula protoze na jejich demu je to vzdycky jenom jedna kategorie
        for orig_token in link_data["tokenized link"][0]:

            for new_token in link_as_tokens:

                if new_token == orig_token:
                    num_of_same_tokens += 1
                    break

        if num_of_same_tokens == len(link_as_tokens):
            possible_candidates.append(link_data["tokenized link"][0])
        elif num_of_same_tokens >= (len(link_data["tokenized link"][0])/2):
            possible_candidates.append(link_data["tokenized link"][0])



    return possible_candidates

def find_candidates_for_file(file_new, file_old):
    """ :param file_new (dictionary) content of the file with new links
        :param file_old (dictionary) content od the file with ols links
        :returns array of tuples(old_link, [new_possible_links])


    """
    array_to_return = []
    for line in file_old.values():

        # we are only using the last part of the link, not the whole link
        possible_cadidates = find_candidates_for_line(file_new, line['tokenized link'][-1])
        # pair = (line, possible_cadidates)
        yield line, possible_cadidates
        # array_to_return.append(pair)


    return array_to_return