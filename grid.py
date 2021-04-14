from math import sqrt
import time
from decimal import *
import random


class GridMatrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rects = []

    def create_rects(self):
        dim_x = self.width // 20
        dim_y = self.height // 20
        for n in range(0, dim_x):
            for m in range(0, dim_y):
                self.rects.append({
                    'coord': [n, m],
                    'grid': [0 + (n * 20), 0 + (m * 20), 20, 20],
                    'screen': None,
                    'color': None,
                    'fill': 1,
                    'wall': 0,
                    'cost': 0
                })
        return self.rects


def log_(logs, position_list, return_list):
    f = open("position_log.txt", "a")
    f.write("_-_-_-_-\n Starting location: " + str(position_list[0]) + "\n")
    f.write("Ending: " + str(position_list[1]) + "\n")
    for _ in return_list:
        f.write(str(_['coord']))
    f.write("\n")
    for log in logs:
        f.write(str(log) + "\n")


def find_nine(coord, rectal_dict, position_list):
    scores = []
    print(position_list)
    a = coord[0] - 1
    b = coord[1] - 1
    y = position_list[1][0] - 1
    z = position_list[1][1] - 1
    current_list = []
    goal_list = []

    def wall_check(wall_num):
        if wall_num[1] is not 1:
            wall_num[2] = 15
            return wall_num
        else:
            return wall_num

    for i in range(0, 3):
        for j in range(0, 3):
            for box in rectal_dict:
                if box['coord'] == [a + j, b + i]:
                    current_list.append([box['grid'], box['wall'], 0])
                if box['coord'] == [y + j, z + i]:
                    goal_list.append([box['grid'], box['wall']])

    checks = {"box_current": current_list[4],
              "box_three": wall_check(current_list[3]),
              "box_one": wall_check(current_list[1]),
              "box_five": wall_check(current_list[5]),
              "box_seven": wall_check(current_list[7])
              }
    carriage = []
    check_counter = 0
    for key in checks:
        if checks[key][2] == 15:
            check_counter += 1
    print(checks)
    print(check_counter)
    if check_counter == 1:
        for _ in checks:
            if checks[_][2] == 15:
                carriage.append(checks[_][0][0]//20)
                carriage.append(checks[_][0][1]//20)

    print(carriage)
    vertex_scores = {}
    return carriage
    # return_list[scores.index(min(scores))]['coord']
