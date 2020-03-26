import csv
import os
import sys


def check_line_argument():
    """ 
    Checks if the supplied command line arguements are correct and valid.
    If there are any errors, return an error message and exit
    """
    error = False

    if len(sys.argv) <= 2:
        sys.stderr.write("Error: insufficient command line arguments\n")
        error = True

    if len(sys.argv) >= 2 and not os.path.isfile(sys.argv[1]):
        sys.stderr.write("Error: file does not exist\n")
        error = True

    if error:
        sys.stderr.write("python3 search.py <csv> [search terms(s)...]\n")
        exit()


def clean(word_list):
    """
    Cleans up a word by removing leading and trailing non-alphanumeric characters

    Parameters
    ----------
    word_list       array   An array of words to be cleaned

    Return
    ------
    new_word_list   array   An array of cleaned words
    """
    new_word_list = []
    for w in word_list:
        while w != "" and not w[-1].isalpha() and not w[-1].isdigit():
            w = w[:-1]
        while w != "" and not w[0].isalpha() and not w[0].isdigit():
            w = w[1:]
        if w != "" and w not in new_word_list:
            new_word_list.append(w)
    return new_word_list


def read_csv():
    """
    Reads in a csv file and creates a dictionary where the key values are terms and the values are the id and title
    If a key is seen in more than one id, then add the id to the set

    Return
    ------
    doc_dict        dict    A dictionary of all of the terms as keys and the id they belong to as values
    """
    doc_dict = {}
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            # Create a set to remove any duplicates from the title and body
            value = clean(set(row[1].lower().split() + row[2].lower().split()))
            for v in value:
                if v in doc_dict:
                    doc_dict[v].add(row[0] + ", " + row[1])
                else:
                    doc_dict[v] = set([row[0] + ", " + row[1]])
    return doc_dict


def find(doc_dict, terms):
    """
    Finds terms that belong in all of docuements

    Parameter
    ---------
    doc_dict        dict    Dictionary of query terms as keys and ids as values
    terms           array   An array of strings to search in the document

    Return
    ------
    ret_set         set     A set of non-duplicate ids that contain all terms
    """
    ret_set = set()
    for t in terms:
        if t.lower() in doc_dict:
            if not bool(ret_set):
                ret_set = doc_dict[t.lower()]
            else:
                # Finds all of the terms in all of the ids
                ret_set = ret_set.intersection(doc_dict[t.lower()])
    return ret_set


def main():
    check_line_argument()
    doc_dict = read_csv()
    id_title = find(doc_dict, sys.argv[2:])
    for i in id_title:
        print(i)


if __name__ == "__main__":
    main()