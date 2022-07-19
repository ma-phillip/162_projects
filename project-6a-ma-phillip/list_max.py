# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 22, 2022
# Description: A recursive function that takes a list of numbers and returns the maximum value

def list_max(list):
    """Takes a list and returns the maximum value of the list"""
    if len(list) == 1:  # base case, when the list is down to the last value
        return list[0]
    if list[0] >= list[1]: # checks which number is larger between two indexes and deletes the smaller
        del list[1]
        return list_max(list)
    if list[1] >= list[0]:
        del list[0]
        return list_max(list)
