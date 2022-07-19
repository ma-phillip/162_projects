# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 15, 2022
# Description: A string sort function that sorts a string list in alphabetical order

def string_sort(string_list):
    """Sorts a string list in alphabetical order, ignoring case"""
    for i in range(1, len(string_list)):
        value = string_list[i]
        pos = i - 1
        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value

