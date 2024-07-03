#!/usr/bin/python3
""" defines method to solve lockboxes problem """


def canUnlockAll(boxes):

    from copy import deepcopy

    # checks valid list of boxes
    if type(boxes) is not list or len(boxes) < 1:
        return False
    # checks whether all boxes contain valid list of keys
    for box in boxes:
        if type(box) is not list:
            return False
    # creates a copy of new boxes
    unlockedBoxes = deepcopy(boxes)
    # calls unlockBox() to open box 0
    # unlockBox() recursively open any boxes with keys from the opened box
    unlockedBoxes = unlockBox(unlockedBoxes, 0)
    # after opening all boxes, check that total boxes have been opened
    # opened boxes are noted with a -1 flag
    for box in unlockedBoxes:
        if -1 not in box:
            # if a box is missing the -1 flag, it wasnt  unlocked
            return False
    # returns true if all boxes in the previous loop were indicated as unlocked
    return True


def unlockBox(boxes, key):

    print(key)
    if type(key) is not int or key < 0:
        # when key is invalid
        return boxes
    # mark that the box has been opened by appeneding a -1 flag

    boxes[key].append(-1)
    # loop through any new keys found in the recently opened box

    for new_key in boxes[key]:
        if new_key is -1:
            # if new key is the flag for an opened box, continue
            continue
        if new_key >= len(boxes):
            # if new key is out of range of the available boxes, continue
            continue
        if -1 in boxes[new_key]:
            # if the box has previously been opened, continue
            continue
        # update the list of boxes by calling unlockBox() to open new boxes
        boxes = unlockBox(boxes, new_key)
    # after unlocking all boxes with the available keys, return boxes
    return boxes
