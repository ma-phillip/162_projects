# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 16, 2022
# Description: Takes a .txt file containing a list of numbers, sums the numbers and writes the sum in a new .txt file

def file_sum(txt_file):
    """Takes as parameter a .txt file containing a list of numbers. Adds the numbers together into a total sum and
    writes the total sum as a string to a new .txt file"""
    total_sum = 0
    with open(txt_file, 'r') as numbers:
        for line in numbers:
            total_sum += float(line)

    str_sum = str(total_sum)

    with open('sum.txt', 'w') as new_file:
        new_file.write(str_sum)

