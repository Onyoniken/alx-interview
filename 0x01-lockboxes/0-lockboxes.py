#!/usr/bin/python3
""" defines method to solve lockboxes problem """


def canUnlockAll(boxes):

    from copy import deepcopy

    # checks if given valid list of boxes
    if type(boxes) is not list or len(boxes) < 1:
        return False
    for box in boxes:
        if type(box) is not list:
            return False
    copyBoxes = deepcopy(boxes)
    keys_list = [0]
    while len(keys_list) > 0:
        key = keys_list[0]
        keys_list = keys_list[1:]
        if type(key) is not int or key < 0:
            return False
        copyBoxes[key].append(-1)
        for new_key in copyBoxes[key]:
            if new_key == -1:
                continue
            if new_key >= len(copyBoxes):
                continue
            if -1 in copyBoxes[new_key] or new_key in keys_list:
                continue
            keys_list.append(new_key)
    for box in copyBoxes:
        if -1 not in box:
           
            return False
    return True
