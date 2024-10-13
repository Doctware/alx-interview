#!/usr/bin/python3
""" this module contains a method thas return True if given box cen be open
    otherwise return Flase """


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    :param boxes: List of lists, where each list contains
     the keys for other boxes
    :return: True if all boxes can be opened, otherwise False
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is initially unlocked
    keys = [0]  # Start with the keys from box 0

    while keys:
        current_key = keys.pop()  # Get the next key
        for key in boxes[current_key]:
            # If the key opens a valid and locked box
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                keys.append(key)  # Add the keys from this box

    return all(unlocked)  # Return True if all boxes are unlocked
