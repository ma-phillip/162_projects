# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: March 28, 2022
# Description: Imports statistics module, creates a class Student containing name and grade and calculates the mean, median and mode of grades from a list
import statistics as stats

class Student:
    '''Create a class with two private data members: name and grade'''
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        '''Returns grade'''
        return self._grade

def basic_stats(student_list):
    '''Takes a list of Student objects, calculates and returns mean, median, and mode'''
    scores = [s.get_grade() for s in student_list]
    mean = stats.mean(scores)
    median = stats.median(scores)
    mode = stats.mode(scores)

    data = (mean, median, mode)
    return data
