"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    
    find_greatest_number = max(incoming_list)
    return find_greatest_number

    pass


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    find_least_number = min(incoming_list)
    return find_least_number

    pass


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    add_list_numbers = sum(incoming_list)
    return add_list_numbers
    
    pass


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """

    longest_value_key = max(incoming_dict, key=incoming_dict.get)
    return longest_value_key

    pass
