# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 24, 2022
# Description: A function that takes a list of nonzero integers as a parameter. The position starts at the zero index
# of the list and tries to reach the end of the list by adding or subtracting its current position. Uses memoization
# to remember all the indexes visited.

def row_puzzle(puzzle_list, pos=0, memo=None):
    """Takes a list of nonzero integers as a puzzle. Initializes the position to the 0 index and initializes memo to
    None """
    if memo is None:  # makes an empty list for all indices visited
        memo = []

    if pos == (len(puzzle_list) - 1):  # base case for when the last index is reached
        return True

    if pos in memo:  # base case for when the current position has already been visited
        return False

    if pos == 0 and puzzle_list[0] < len(puzzle_list):
        # takes the initial position and checks to make sure the integer at index 0 won't cause pos to go over the
        # list. Adds the 0 index to visited and adds the integer to the position
        memo.append(pos)
        pos += puzzle_list[0]
        return row_puzzle(puzzle_list, pos, memo)

    if (pos + puzzle_list[pos]) < len(puzzle_list) and (pos - puzzle_list[pos]) > 0:
        # if the current position index integer can go both left and right, add the current pos to the list visited
        # and go both left and right
        memo.append(pos)
        return row_puzzle(puzzle_list, pos + puzzle_list[pos], memo) or row_puzzle(puzzle_list, pos - puzzle_list[pos],
                                                                                   memo)

    if (pos + puzzle_list[pos]) < len(puzzle_list):
        # if the current position index integer can only go right, add the current pos to the list visited
        # and go right by adding the integer to pos
        memo.append(pos)
        return row_puzzle(puzzle_list, pos + puzzle_list[pos], memo)

    if (pos - puzzle_list[pos]) > 0:
        # if the current position index integer can only go left, add the current pos to the list visited
        # and go left by subtracting the integer from pos
        memo.append(pos)
        return row_puzzle(puzzle_list, pos - puzzle_list[pos], memo)

    else:
        return False

