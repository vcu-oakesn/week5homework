"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    
    incoming_list = [1, 2, 3]
    return max(incoming_list)

    pass


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    incoming_list = [4, 5, 6]
    return min(incoming_list)

    pass


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    incoming_list = [7, 8, 9, 10]
    return sum(incoming_list)
    
    pass


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    # Dictionary includes pop artists with the highest album sales (in millions)
    incoming_dict = {
        'Beatles': 283.2, 
        'Elvis Presley': 227.3, 
        'Michael Jackson': 236.6, 
        'Elton John': 194.7, 
        'Madonna': 178.9}
    return max(incoming_dict, key=incoming_dict.get)

    pass
