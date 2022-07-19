# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 22, 2022
# Description: A recursive function that takes two strings and checks if the first is a subsequence
# of the second and returns True if it is and False if it is not

def rec_is_subsequence(string_1, string_2, len1, len2):
    """Takes two strings and the lengths of the strings as parameters and checks to see if the
    first is a subsequence of the second."""
    # len1 = length of string_1
    # len2 = length of string_2
    if len1 == 0:  # base case for when all of string_1 has been compared to string_2
        return True

    if len2 == 0:  # base case for when all of string_2 has been compared to string_1
        return False

    if string_1[len1 - 1] == string_2[len2 - 1]:  # if letters at the end of both strings are equal
        return rec_is_subsequence(string_1, string_2, len1 - 1, len2 - 1)  # move onto next letters of both strings

    if string_1[len1 - 1] != string_2[len2 - 1]:  # if letters at both ends aren't equal
        return rec_is_subsequence(string_1, string_2, len1, len2 - 1) # move onto next letter in string_2


def is_subsequence(string_1, string_2):
    """A helper function so user does not need to input length of the strings"""
    return rec_is_subsequence(string_1, string_2, len(string_1), len(string_2))
