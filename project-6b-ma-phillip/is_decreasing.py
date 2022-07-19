# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 22, 2022
# Description: A recursive function that takes a list of numbers and returns True if the elements are
# strictly decreasing and False if otherwise

def is_decreasing(list):
    """Takes a list of numbers and returns True if strictly decreasing and false if not"""
    if len(list) == 1:  # base case if the whole list is decreasing
        return True

    if list[0] > list[1]:  # if first two elements are decreasing, removes the first element and checks remaining list
        del list[0]
        return is_decreasing(list)

    if list[0] <= list[1]:  # base case if there are nondecreasing elements
        return False
