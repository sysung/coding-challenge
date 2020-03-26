import csv
import os
import sys


def check_line_argument():
    """ 
    Checks if the supplied command line arguements are correct and valid.
    If there are any errors, 
    """
    error = False

    if len(sys.argv) < 3:
        sys.stderr.write("Error: insufficient command line arguments\n")
        error = True

    if len(sys.argv) > 2 or not os.path.isfile(sys.argv[1]):
        sys.stderr.write("Error: file does not exist\n")
        error = True

    if error:
        sys.stderr.write("python3 search.py <csv> [search terms(s)...]\n")
        exit()


def clean(word_list):
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
    doc_dict = {}
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            value = clean(set(row[1].lower().split() + row[2].lower().split()))
            for v in value:
                if v in doc_dict:
                    doc_dict[v].add(row[0] + ", " + row[1])
                else:
                    doc_dict[v] = set([row[0] + ", " + row[1]])
    return doc_dict


def find(doc_dict, terms):
    ret_set = set()
    for t in terms:
        if t.lower() in doc_dict:
            if not bool(ret_set):
                ret_set = doc_dict[t.lower()]
            else:
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