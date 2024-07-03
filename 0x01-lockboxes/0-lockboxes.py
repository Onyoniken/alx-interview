#!/usr/bin/python3
""" defines method to solve lockboxes problem """


def canUnlockAll(boxes):

    from copy import deepcopy
    # checks if given valid list of boxes
    if type(boxes) is not list or len(boxes) < 1:
        return False
    # checks whether all boxes contain valid list of keys
    for box in boxes:
        if type(box) is not list:
            return False
        #creates copy boxes not affecting the original lists
    copyBoxes = deepcopy(boxes)
    keys_list = [0]
    # while there are available keys
    while len(keys_list) > 0:
        # current one will be the first available
        key = keys_list[0]
        # Keys reset to remove used key
        keys_list = keys_list[1:]
        # checks for valid key
        if type(key) is not int or key < 0:
            return False
        # Mark opened boxes by appending -1
        copyBoxes[key].append(-1)
        for new_key in copyBoxes[key]:
            if new_key == -1:
                continue
            if new_key >= len(copyBoxes):
                continue
            if -1 in copyBoxes[new_key] or new_key in keys_list:
                continue
            keys_list.append(new_key)
    # After opening all boxes, checks all boxes have been opened
    for box in copyBoxes:
        if -1 not in box:
            # if box missing in -1, it wanst unlocked
           
            return False
    return True
