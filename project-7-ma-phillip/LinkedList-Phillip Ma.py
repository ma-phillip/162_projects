# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: May 9, 2022
# Description: A Linked List class that contains recursive methods for add, remove, contains, insert and reverse
# methods. Also contains a recursive method to_plain_list that returns a regular python list from the linked list.
class Node:
    """Contains two data members, data and next"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A class that can add and remove items from a linked list recursively. Can also check if the linked list contains
    a given parameter and can insert and remove the list. Also contains a function that returns a regular python list from
    the linked list"""
    def __init__(self):
        self._head = None

    def get_head(self):
        """Returns the head of the list"""
        return self._head

    def rec_add(self, val, node):
        """Recursively adds a value to the end of a linked list"""
        if node.next is None:
            node.next = Node(val)
        else:
            self.rec_add(val, node.next)

    def add(self, val):
        """Helper function so the user does not have to input the initial head of the linked list"""
        if self._head is None:
            self._head = Node(val)
        else:
            node = self._head
            self.rec_add(val, node)

    def rec_remove(self, val, node):
        """Recursively searches and removes a provided value from the linked list"""
        if node.next is None:
            return
        elif node.next.data == val:
            node.next = node.next.next
            return
        else:
            self.rec_remove(val, node.next)

    def remove(self, val):
        """Helper function so the user does not have to input the head of the linked list. Also checks if
        the provided value is the head of the function."""
        if self._head is None:
            return
        if self._head.data == val:
            self._head = self._head.next
            return
        node = self._head
        self.rec_remove(val, node)

    def rec_contains(self, val, node):
        """Recursively checks to see if a provided value is contained in the linked list and returns True
        if contained and False if not."""
        if node.next is None:
            if node.data == val:
                return True
            else:
                return False
        if node.data == val:
            return True
        else:
            return self.rec_contains(val, node.next)

    def contains(self, val):
        """Helper function so the user does not have to input the head of the list. Also checks to see if
        the provided value is the head of the list and returns True if it is."""
        if self._head.data == val:
            return True
        else:
            node = self._head
            return self.rec_contains(val, node)

    def rec_insert(self, val, pos, node, starting_pos):
        """Recursively inserts a given value into a given position of a linked list. Adds value to end of the list
        if the given position is longer than the linked list."""
        if node.next is None:
            node.next = Node(val)
            return
        elif pos == starting_pos+1:
            temp = node.next
            new_node = Node(val)
            node.next = new_node
            new_node.next = temp
        else:
            print(starting_pos)
            self.rec_insert(val, pos, node.next, starting_pos+1)

    def insert(self, val, pos):
        """Helper function so the user does not have to enter the head of the list and the starting position of 0.
        Checks of the given position is 0 and inserts the provided value as the new head."""
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
            return
        elif self._head.next is None:
            self._head.next = Node(val)
            return
        else:
            node = self._head
            starting_pos = 0
            self.rec_insert(val, pos, node, starting_pos)

    def rec_reverse(self, node, previous):
        """Recursively reverses the linked list"""
        if node.next is None:
            node.next = previous
            return node
        next = self.rec_reverse(node.next, node)
        node.next = previous
        return next

    def reverse(self):
        """Helper function so the user does not have to enter any parameters. Makes the final value of the linked list
        the new head"""
        node = self._head
        previous = None
        self._head = self.rec_reverse(node, previous)

    def rec_to_plain_list(self, node, plain_list):
        """Returns a python list containing the same value and order of the linked list."""
        if node.next is None:
            plain_list.append(node.data)
            return plain_list
        plain_list.append(node.data)
        self.rec_to_plain_list(node.next, plain_list)

    def to_plain_list(self):
        """Helper function so that the user doesn't have to intialize an empty python list and the head of the list."""
        node = self._head
        plain_list = []
        self.rec_to_plain_list(node, plain_list)
        return plain_list

