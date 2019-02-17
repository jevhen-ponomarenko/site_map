from parser import parse_file
from parser import load_file_as_array_of_pairs
import compare
import tokenizer
import time
import colored
from colored import stylize

if __name__ == "__main__":
    # green = colored.fg("green") + colored.attr("bold")
    # red = colored.fg("red") + colored.attr("bold")
    # # old_links = parse_file('old.csv')
    # # new_links = parse_file('new.csv')
    #
    # old_links = parse_file('data/old.csv')
    # new_links = parse_file('data/new.csv')
    #
    # candidates = compare.find_candidates_for_file(new_links, old_links)
    #
    # for pair in candidates:
    #     orig_link = tokenizer.detokenize_line(pair[0]['tokenized link'])
    #
    #     print('link')
    #     print(stylize(orig_link, green))
    #     print('candidates :')
    #     for candidate in pair[1]:
    #         new_link = tokenizer.detokenize_line(candidate)
    #         print(stylize(new_link, red))
    #         print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    #     print('--------------------------------------------------------')
    old_links = parse_file('data/old.csv')
    new_links = parse_file('data/new.csv')
    good = 0
    bad = 0
    actual_data = load_file_as_array_of_pairs('data/URL_protruck.csv')

    candidates = compare.find_candidates_for_file(new_links, old_links)
    time_start = time.time()
    for pair in candidates:
        orig_link = tokenizer.detokenize_line(pair[0]['tokenized link'])


        for line in actual_data:
            # found desired line in

            old_link = line[1].replace('\n', '')
            if orig_link == old_link:
                old_good = good
                for link in pair[1]:
                    link = tokenizer.detokenize_line(link)
                    if link + '/' == line[0]:
                        good += 1
                        print('found {0} of {1} links'.format(good, len(actual_data)))
                        print('time between successful calls: {0}'.format(time.time() - time_start))

                if good == old_good:
                    print(" for link {0}".format(tokenizer.detokenize_line(pair[0]['tokenized link'])))
                    for link in pair[1]:
                        print('candidate {0}'.format(tokenizer.detokenize_line(link)))

    print('good: ')
    print(good)
    print('total: {0}'.format(len(actual_data)))