from parser import parse_file
from compare import find_possible_candidates

if __name__ == "__main__":
    old_links = parse_file('old.csv')
    new_links = parse_file('new.csv')

    # old_links = parse_file('old_test.csv')
    # new_links = parse_file('new_test.csv')

    for link in old_links.values():

        print('link:')

        for token in link["tokenized link"]:
            print(token)

        print('possible candidates:')

        for candidate in find_possible_candidates(new_links, link["tokenized link"][-1]):
            print(candidate)

        print('---------------------------')

#TODO: \n na konci token contentu je treba vymazat