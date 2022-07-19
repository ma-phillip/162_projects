# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: May 13, 2022
# Description: A generator function that generates a sequence that counts how many there are of each digit
# (in a row) in the previous term (starting with 2). Goes indefinitely and yields string values

def count_seq():
    """A generator function that starts at 2 and yields a string value that counts how many of a previous digit
    there are, starting with 2"""
    num = '2'
    while int(num) > 0:   # will always be true so goes indefinitely
        yield num
        new_value = ''
        while len(num) > 0:
            first = num[0]
            total = 0
            while len(num) > 0 and num[0] == first:
                total += 1
                num = num[1:]
            new_value += str(total) + first
        num = new_value

