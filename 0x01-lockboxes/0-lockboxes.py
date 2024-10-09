#!/usr/bin/python3
"""
Contains the lockboxes problem solution
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes entered can be unlocked
    Args:
        boxes (list of lists): a list containing boxes(lists)
    Return:
        Boolean: True if all boxes can be unlocked, false otherwise
    """
    num_boxes = len(boxes)
    opened = set([0])
    keys = set(boxes[0])

    while keys:
        box = keys.pop()
        if box not in opened:
            opened.add(box)
            keys.update({key for key in boxes[box] if key not in opened})

    return len(opened) == num_boxes
