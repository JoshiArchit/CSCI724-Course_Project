"""
Filename : property_name_match.py
Author : Archit Joshi (aj6082), Athina Stewart (as1896)
Date Created : 3/21/2024
Description : This script compares the names of the properties of the parameters
in the post requests of document 1 against the names of the properties of the parameters
of the parameters in document 2.
Link to the original paper: https://ieeexplore.ieee.org/document/9885779
Language : python3
"""

import json
import os
import time


def compare_dicts(dict1, dict2):
    """
    This function compares the keys of the parameters in the post requests of
    doc_1 against the keys of the parameters in the get requests of doc_2. If the
    keys of the post parameters are exactly the same as the keys of the get
    parameters, return True
    :param dict1: post request dictionary
    :param dict2: get request dictionary
    :return: True if the keys of the post parameters are exactly the same as the keys of the get parameters
    """
    # if the keys of dict1 are exactly the same as the keys of
    # dict2, return True
    if dict1.keys() == dict2.keys():
        return True


def match_property_names(doc_1, doc_2):
    """
    This function compares the names of the properties of the parameters
    in the post requests of doc_1 against the names of the properties
    of the parameters in doc_2
    :param doc_1: first API description
    :param doc_2: second API description
    :return:
    """
    total_match_count = 0

    for method_type in doc_1:
        for operation_type in doc_1[method_type]:
            if "post" in operation_type:
                post_parameters = doc_1[method_type][operation_type]
                for method_type_2 in doc_2:
                    for operation_type_2 in doc_2[method_type_2]:
                        if "get" in operation_type_2:
                            get_parameters = doc_2[method_type_2][operation_type_2]
                            # compare the keys of the post parameters with the keys
                            # of the get parameters
                            # if all the keys of the post parameters are in the get
                            # parameters, increment the match count by 1
                            if compare_dicts(post_parameters, get_parameters):
                                total_match_count += 1
    return total_match_count


def compare_all_docs():
    """
    This function compares all the documents in the post collection with all the documents in the get collection
    :return: total match count
    """
    num_post_docs_examined = 0
    total_match_count = 0

    # iterate through each document in the post_requests folder found in the local directory
    for filename in os.listdir("post_requests"):
        with open(f"post_requests/{filename}", 'r') as post_file:
            post_doc = json.load(post_file)
            # iterate through each document in the get_requests folder found in the local directory
            for filename in os.listdir("get_requests"):
                with open(f"get_requests/{filename}", 'r') as get_file:
                    get_doc = json.load(get_file)
                    total_match_count += match_property_names(post_doc, get_doc)
            num_post_docs_examined += 1
            print(f"Number of post documents examined: {num_post_docs_examined}")
            print(f"Total match count: {total_match_count}")
            print("--------------------------------------------------")
            print("\n")
    return total_match_count


def main():
    start_time = time.time()
    print(f"Number of post-get matches = {compare_all_docs()}")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
