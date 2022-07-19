# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 15, 2022
# Description: Two sort functions that return a count of comparisons and exchanges used
def bubble_count(a_list):
    """Sorts a_list in ascending order via bubble sort, counts how many comparisons and exchanges are made
  and returns a tuple containing those values"""
    comparisons = 0
    exchanges = 0
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
                exchanges += 1
    results = (comparisons, exchanges)
    return results


def insertion_count(a_list):
    """Sorts a_list in ascending order via insertion sort, counts how many comparisons and exchanges are made
  and returns a tuple containing those values"""
    comparisons = 0
    exchanges = 0
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            exchanges += 1
            comparisons += 1
        a_list[pos + 1] = value
    results = (comparisons, exchanges)
    return results
