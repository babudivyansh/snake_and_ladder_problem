"""
@Author: Divyansh Babu

@Date: 2021-12-05 11:33

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-12-05 11:33

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
        Description: implementation of function for repeat till the plyer reaches the winning position and every move is
        displayed.

        Parameter: None

        Return: Dice value(int type)
    """
    player_opt = random.randint(0, 2)
    dice_vlu = roll_die_1_to_6()
    if player_opt == 1:  # Ladder
        return dice_vlu
    elif player_opt == 2:  # Snake
        return -dice_vlu
    else:  # no play
        return 0


def two_player():
    """
        Description: implementation of function to play the game with two player.

        Parameter: None

        Return: None
    """
    player_pos1 = 0
    player_pos2 = 0
    option = 1
    while player_pos1 < 100 and player_pos2 < 100:
        match option:
            case 1:
                dice = play()
                if dice > 0:
                    if player_pos1 + dice > 100:
                        pass
                    else:
                        player_pos1 += dice
                    option = 1
                    continue
                else:
                    player_pos1 += dice
                    if player_pos1 < 0:
                        player_pos1 = 0
                    option = 2
            case 2:
                dice1 = play()
                if dice1 > 0:
                    if player_pos2 + dice1 > 100:
                        pass
                    else:
                        player_pos2 += dice1
                    option = 2
                else:
                    player_pos2 += dice1
                    if player_pos2 < 0:
                        player_pos2 = 0
                    option = 1
        print(f"player 1 position is: {player_pos1}\t\tplayer 2 position is: {player_pos2}")

    if player_pos1 == 100:
        print(f"Player 1 is win!! at position {player_pos1}")
    else:
        print(f"Player 2 is win!! at position {player_pos2}")


if __name__ == '__main__':
    two_player()
