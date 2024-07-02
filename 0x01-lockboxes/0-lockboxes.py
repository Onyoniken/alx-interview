#!/usr/bin/python3


def canUnlockAll(boxes):

    length = len(boxes)	# Number of boxes
    keys = set()	# Set to store keys collected
    opened_boxes = []	# List to track which boxes have been opened
    k = 0		# Start with the first box (index 0)

# Loop until all reachable boxes have been opened

    while k < length:
        oldi = k
        opened_boxes.append(k)	# Mark the current box as opened
        keys.update(boxes[k])	# Collect all keys from the current box

	# Check all collected keys
        for key in keys:
	
	# If the key points to a valid unopened box, move to that box
            if key != 0 and key < length and key not in opened_boxes:
                k = key
                break

	# If no new box was opened, break out of the loop
        if oldi != k:
            continue
        else:
            break

	 # Check if all boxes except the first one have been opened
    for k in range(length):
        if k not in opened_boxes and k != 0:
            return False

    return True
