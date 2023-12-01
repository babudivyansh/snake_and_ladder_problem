"""
@Author: Divyansh Babu

@Date: 2021-12-01 12:30

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-12-01 12:30

@Title : Snake and Ladder Problem.
"""
import random


def single_ply_at_pos_0():
    """
        Description: implementation of Snake and Ladder game played with single player at start position 0.

        Parameter: None

        Return: position 0
    """

    return 0


def roll_die_1_to_6():
    """
        Description: implementation of function for The Player rolls the die to get a number between 1 and 6.

        Parameter: None

        Return: position result
    """
    result = random.randint(1, 6)
    return result


if __name__ == '__main__':
    print(single_ply_at_pos_0())
    print(roll_die_1_to_6())
