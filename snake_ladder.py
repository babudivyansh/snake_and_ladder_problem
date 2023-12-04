"""
@Author: Divyansh Babu

@Date: 2021-12-04 12:15

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-12-04 12:15

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

        Return: Random number for die.
    """

    return random.randint(1, 6)


def play():
    """
        Description: implementation of function for repeat till the plyer reaches the winning position.

        Parameter: None

        Return: None
    """
    position = 0
    while position <= 100:
        player_opt = random.randint(0, 2)
        dice_vlu = roll_die_1_to_6()
        if player_opt == 0:
            print("If not playing then player stays at same position")
        elif player_opt == 1:
            position += dice_vlu
            print(f"Player moves ahead by: {dice_vlu}")
            if position > 100:
                position -= dice_vlu
            elif position == 100:
                print("Player wins!!")
                break
        elif player_opt == 2:
            position -= dice_vlu
            print(f"Player moves behind by: {dice_vlu}")
            if position < 0:
                position = 0
        print(f"Current Position is:{position}")


if __name__ == '__main__':
    play()
