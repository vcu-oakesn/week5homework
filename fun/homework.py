"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    
    w = max(incoming_list)
    return w

    pass


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    x = min(incoming_list)
    return x

    pass


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    if incoming_list: 
        y = sum(incoming_list)
    else
        y = 0
    return y
    
    pass


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """

    # z = max(incoming_dict, key=incoming_dict.get)
    # z = max(incoming_dict, key=len)
    
    if not incoming_dict
        return None

    all_keys = incoming_dict.keys()
    if not all_keys
        return None

    key_with = None
    for keys in all_keys
        if not key_with:
            key_with = key

        if len(incoming_dict[key]) > len(incoming_dict[key_with]):
            key_with = key

    return key_with

    pass
