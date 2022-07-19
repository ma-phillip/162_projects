# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 14, 2022
# Description: Modifies the given binary search function so that an error is raised instead of -1
class TargetNotFound(Exception):
    """Error to be raised if target is not in the list """
    pass


def bin_except(a_list, target):
    """Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, raises TargetNotFound, indicating the target value isn't in the list"""
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound


