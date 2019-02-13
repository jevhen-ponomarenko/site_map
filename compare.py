from parser import parse_file


def find_possible_candidates(file_as_dict, link_as_tokens):
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
                else:
                    continue

        if num_of_same_tokens == len(link_as_tokens):
            possible_candidates.append(link_data["tokenized link"][0])
        elif num_of_same_tokens >= (len(link_data["tokenized link"][0])/2 ):
            possible_candidates.append(link_data["tokenized link"][0])



    return possible_candidates
