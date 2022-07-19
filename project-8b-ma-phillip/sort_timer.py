# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: May 16, 2022
# Description: Times how long a bubble sort and insert sort algorithm take to complete various list sizes. Graphs those times in
# a graph

import functools
import time
import random
from matplotlib import pyplot


def sort_timer(func):
    """A decorator function that times how long a function takes to complete and returns that time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        beginning = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - beginning

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a_list in ascending order. Is decorated with sort_timer"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order. Is decorated with sort_timer"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(bubble, insert):
    """Compares how long bubble sort vs insert sort takes using a graph"""
    bubble_list = []
    insert_list = []

    def get_points(starting_list, initial_value):
        """A recursive function that creates an increasing list of random integers and adds how long each
        sort method takes to their respective list"""
        list_1 = []
        if starting_list == 11:
            return
        else:
            for n in range(initial_value):
                list_1.append(random.randint(0, 10000))
            list_2 = list(list_1)
            bubble_list.append(bubble(list_1))
            insert_list.append(insert(list_2))
            get_points(starting_list + 1, initial_value + 1000)

    get_points(1, 1000)
    x_coordinates = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    pyplot.plot(x_coordinates, bubble_list, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(x_coordinates, insert_list, 'go--', linewidth=2, label='Insert Sort')
    pyplot.xlabel("Numbers Sorted")
    pyplot.ylabel("Time To Sort (in seconds)")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)