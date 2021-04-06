from math import sqrt
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


def find_nine(coord, rectal_dict, position_list):
    scores = []
    a = coord[0] - 1
    b = coord[1] - 1
    y, z = position_list[1]
    return_list = []
    for i in range(0, 3):
        for j in range(0, 3):

            for rectal in rectal_dict:
                if rectal['coord'] == [a + i, b + j]:
                    return_list.append(rectal)
    log_list = []
    for k in return_list:
        w, x = k['coord']
        tally = float((sqrt((y - w) ** 2 + (z - x) ** 2)) * 10)
        wall = 1000
        past = 7
        tally += float(round(random.uniform(0.5, 1.0), 2))
        log_list.append((k['coord'], tally))
        if k['coord'] in position_list:
            tally += past
        if k['coord'] == position_list[1]:
            tally = 0

        if k['wall'] == 1:
            tally += wall

        scores.append(tally)
        log_list.append((k['coord'], tally))
    f = open("position_log.txt", "a")
    f.write("Starting location: " + str(position_list[0]) + "\n")
    f.write("Ending: " + str(position_list[1]) + "\n")
    for _ in return_list:
        f.write(str(_['coord']))
    f.write("\n")
    for log in log_list:
        f.write(str(log) + "\n")

    return return_list[scores.index(min(scores))]['coord']
