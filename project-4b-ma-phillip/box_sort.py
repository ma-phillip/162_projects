# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 15, 2022
# Description: A box class that contains 3 parameters with get functions as well as volume
# and a separate sort function, that sorts a list of boxes by descending volume

class Box:
    """A box class that takes 3 parameters and initializes them to private length,
    width, and height. Contains a volume method that returns the volume of the box
    as well as get methods for height, length, width"""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        vol = self._length * self._width * self._height
        return vol

    def get_length(self):
        return self._length

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width


def box_sort(list_of_boxes):
    """A function that uses insertion sort to sort a list of boxes from greatest volume
    to least volume"""
    for box in range(1, len(list_of_boxes)):
        value = list_of_boxes[box]
        pos = box - 1
        while pos >= 0 and list_of_boxes[pos].volume() < value.volume():
            list_of_boxes[pos + 1] = list_of_boxes[pos]
            pos -= 1
        list_of_boxes[pos + 1] = value

