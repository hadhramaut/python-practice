""" https://www.codewars.com/kata/directions-reduction/train/python """


def dirReduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    new_plan = []
    for d in arr:
        new_plan.pop() if new_plan and new_plan[-1] == opposite[d] else new_plan.append(d)
    return new_plan